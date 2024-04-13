import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()

# Get openAi key
client = OpenAI(api_key=os.environ.get("API_KEY"))

#Pass in Model params
MODEL = "gpt-4"                                                     # delcares & holds model type
response = client.chat.completions.create(
    model = MODEL,
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what happened to magelian whe he tried to sail around the world."},
    ],
    temperature = 0,
)

# Print the responce to terminal
print(response.choices[0].message.content)
