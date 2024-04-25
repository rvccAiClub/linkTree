import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import time

# Gets API key from .env file
load_dotenv()

# Instantiate openAI client (might need to change this when running)
client = OpenAI(api_key=os.environ.get("API_KEY"))


# Declaring the model we want to use from OpenAI "constant/global"
MODEL = "gpt-3.5-turbo"

# Instatiate the chatBot object (we pass in a unique name and gave the model a context point of what it will do.)
clubChatBot = client.beta.assistants.create(
   name = "ARVEE",
   instructions = "You are a friendly and consise assistant who helps new students answer questions about RVCC's A.I. Club.",
   tools = [{"type": "retrieval"}],
   model = MODEL,
   file_ids = ["file-mJKto4SStWzndMjjWpaAmMHj"]

)
# file = client.files.create(
#     file = open ("test.txt", "rb"),
#     purpose = "assistants"
# )
# print(file)

# assistant_id = clubChatBot.id
# print(clubChatBot.id)

# # Instantiate the thread object
# thread = client.beta.threads.create(
#    messages = [
#        {
#            "role": "user",
#            "content": "What does A.I. club do? I'm interested in joining the club!"
#       }
#    ]
# )
# thread_id = thread.id
# print(thread_id)

assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")

#===create message===#
print("")
print("Arvee: Hey, what do you want to know about RVCC's AI Club?")
print("")
print("Say 'Q' to quit chatting with me.")
print("")
user_message = input("User: ")
while user_message != "Q":
    
    def submit_message(assistant_id, thread_id, user_message):
        client.beta.threads.messages.create(
            thread_id = thread_id,
            role = "user",
            content = user_message
            )
        return client.beta.threads.runs.create(
            thread_id = thread_id,
            assistant_id = assistant_id,
            instructions = "Please address the user as user" 
    )

    assistant_message = submit_message(assistant_id, thread_id, user_message)

    def wait_on_run(run, thread_id):
        while run.status == "queued" or run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
                thread_id = thread_id,
                run_id = run.id,
            )
            time.sleep(0.5)
        return run

    run = wait_on_run(assistant_message, thread_id)

    messages = client.beta.threads.messages.list(thread_id = thread_id)
    last_message = messages.data[0]
    response = last_message.content[0].text.value
    print("")
    print("ARVEE: ",response)
    print("")
    user_message = input("User: ")

