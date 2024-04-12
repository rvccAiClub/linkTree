# --- Import OpenAi Api --- #
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os
import time

# --- Get API key from .env file --- #
load_dotenv()


# --- Pass the API KEY --- #
client = OpenAI(api_key=os.environ.get("API_KEY"))

# --- Declare the model --- #
MODEL = "gpt-3.5-turbo-16k"

# --------- Below code is commented out on purpose  --------- #

# --- Initiate the chatBot object (we pass in a unique name and gave the model a context point of what it will do)--- #
#clubChatBot = client.beta.assistants.create(
    #name="ARVEE",
    #instructions= """You are a friendly and concise assistant who helps new students answer questions about RVCC A.I. Club.""",
    #model=MODEL
    #)


# --- Create our Assistant --- #
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

# --------- Above code is commented out on purpose --------- #

assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")


 # --- Create a message --- #
 # ---Ask a question that will be passed to the OpenAI API --- #
MESSAGE = "What do you think about college? Is it a good investment?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=MESSAGE)

 # --- Run the Application (And address the user as "User name") --- #
run = client.beta.threads.runs.create(
   thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Sebastian")

# --- Time Parameters --- #

def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

run = wait_on_run(run, thread_id)


# --- Print the Response of the ChatBot ARVEE Answering the Question --- #
messages = client.beta.threads.messages.list(thread_id = thread_id)
last_message = messages.data[0]
response = last_message.content[0].text.value
print(response) 
