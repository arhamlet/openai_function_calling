from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


# response = client.responses.create(
#     model = "gpt-4o-mini",
#     instructions = "Talk like a pirate",
#     input = "Are semicolons optional in JavaScript?"
# )
#
# print(response.output_text)


# response = client.responses.create(
#     model = "gpt-4o-mini",
#     input = [
#         {"role": "system", "content": "TALK like a PIRATE"},
#         {"role": "developer", "content":"Don't talk like a pirate"},
#         {"role": "user", "content":"Are semicolons optional in javascript"},
#     ]
# )
#
# print(response.output_text)


response = client.responses.create(
    model = "gpt-4o-mini",
    input = [
        {"role": "system", "content":"Don't Talk like a pirate"},
        {"role": "developer", "content":"talk like a pirate"},
        {"role": "user", "content":"Are semicolons optional in javascript"},
    ]
)

print(response.output_text)