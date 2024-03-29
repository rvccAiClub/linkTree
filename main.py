import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

# Gets Api key from .env file
load_dotenv()

# Instantiate openAI client (might need to change this when running)
client = OpenAI(api_key=os.environ.get("API_KEY"))

# Declaring the model we want to use from OpenAi
MODEL = "gpt-3.5-turbo"

# Instatiate the chatBot object(we pass in a unieque name and gave the model a context point of what it will do)
# clubChatBot = client.beta.assistants.create(
#     name = "ARVEE",
#       instructions = """You are a friendly and concise assistant who helps new students answer questions about RVCC's A.I Club. """,
# model = MODEL
# )

# asistant_id = clubChatBot.id
# print(clubChatBot.id)

# # Instantiate the thread object
# thread = client.beta.threads.create(
# messages = [
#     {
#         "role": "user",
#         "content": "What does A.I club do? I'm interested in joining the club!" 
#         }
#     ]
# )
# thread_id = thread.id
# print(thread_id)

# video timestamp
assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")

MESSAGE = "What do you think about college? Is it a good investment?"
message = client.beta.threads.messages.create(
    thread_id = thread_id,
    role = "user",
    content = MESSAGE
)

run = client.beta.threads.runs.create(
    thread_id = thread_id,
    assistant_id = assistant_id,
    instructions = "Please address the user as German"
)

messages = client.beta.threads.messages.list(thread_id = thread_id)
last_message = messages.data[0]
response = last_message.content[0].text.value
print(response)