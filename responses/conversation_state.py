from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input = "tell me a joke",
    store = True,
)

print(response.output_text)

second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input = [
        {
            "role": "user", "content" : "explain why is this funny?",
        }
    ]
)