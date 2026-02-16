from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


# response = client.responses.create(
#     model = "gpt-4o-mini",
#     input = "write a one sentence bedtime story"
# )
#
# print(response.output_text)


stream = client.responses.create(
    model = "gpt-4o-mini",
    input = "Say 'double bubble bath' ten times really fast",
    stream = True,
)

text_chunks = []
for event in stream:
    if hasattr(event, 'type') and "text.delta" in event.type:
        text_chunks.append(event.delta)
        print(event.delta, end="", flush=True)