# --------------------------------------------------------------
# Import Modules
# --------------------------------------------------------------

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, timedelta
# --------------------------------------------------------------
# Load API Key
# --------------------------------------------------------------

load_dotenv()
client = OpenAI()

# --------------------------------------------------------------
# 1️⃣ Normal LLM Call
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    input="When's the next flight from Amsterdam to New York?",
)

print("\n--- Normal Response ---")
print(response.output[0].content[0].text)

print("\nToken Usage:")
print("Total tokens:", response.usage.total_tokens)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)


# --------------------------------------------------------------
# 2️⃣ Modern Function Calling (Tools API)
# --------------------------------------------------------------

tools = [
    {
        "type": "function",
        "name": "get_flight_info",   # ✅ MUST be top-level
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. AMS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. JFK",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]

user_prompt = "When's the next flight from Amsterdam to New York?"

response = client.responses.create(
    model="gpt-4o-mini",
    input=user_prompt,
    tools=tools,
)

print("\n--- Tool Call Response ---")

for item in response.output:
    if item.type == "tool_call":
        print("Function Name:", item.name)
        print("Arguments:", json.dumps(item.arguments, indent=2))


def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)