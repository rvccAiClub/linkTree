# --- Import OPENAI API --- #
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os

# --- Get API key from .env file --- #
load_dotenv()


# --- Pass the API KEY --- #
client = OpenAI(api_key=os.environ.get("API_KEY"))

# --- Declare the model --- #
MODEL = "gpt-3.5-turbo-16k"


# Initiate the chatBot object (we pass in a unique name and gave the model a context point of what it will do)#
#clubChatBot = client.beta.assistants.create(
    #name="ARVEE",
    #instructions= """You are a friendly and concise assistant who helps new students answer questions about RVCC A.I. Club.""",
    #model=MODEL
    #)


# Create our Assistant #
#assistants_id = clubChatBot.id
#print(clubChatBot.id)


 # --- Create Thread --- #
#thread = client.beta.threads.create(
   # messages= [
     #  {
           # "role": "user",
          #"content": "What does the A.I club do?"
     #  }
  # ]
   # )


 # --- Initiate the thread --- #
#thread_id = thread.id
#print(thread_id)


# Video Timestamp #

assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")


 # --- Create a message --- #
MESSAGE = "What do you think about college? Is it a good investment?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=MESSAGE
)

 ### --- Run the Application --- ###
run = client.beta.threads.runs.create(
   thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Sebastian")


# --- Create the second message (Change this later) --- #
messages = client.beta.threads.messages.list(thread_id = thread_id)
last_message = messages.data[0]
response = last_message.content[0].text.value
print(response) 
