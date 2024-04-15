import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import requests 
import json


load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
MODEL ="gpt-3.5-turbo-16k"

#chatBot = client.beta.assistants.create(
   # name = "Chat Bot",
   # instruction="You will help students learn about the AI Club",
    #  model=MODEL
#)

#assistant_id= chatBot.id
#print(assistant_id)

#Thread
#thread = client.beta.threads.create (
     #messages=[
        # {
            # "role":"user",
           # "content":"How I start managing my time"
        # }
     #]
 #) 


#thread_id = thread.id
#print(thread_id)

assistant_id = os.environ.get("ASST_ID")
thread_id = os.environ.get("THREAD_ID")


# ==== Create a Message =====
MESSAGE = "What is a AI club"
message = client.beta.threads.messages.create(
    thread_id = thread_id,
    role="user",
    content=MESSAGE
)

#=== Run our Assistant===#
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as a student"
)


def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = run.id,
        )
        time.sleep(0.5)
    return run

run = wait_on_run(run, thread_id)

#---Creating second message------#
message = client.beta.threads.messages.list(thread_id = thread_id)
last_message = message.data[0]
response = last_message.content[0].text.value
print(response)

run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id = run.id)

news_api_key = os.environ.get("NEWS_API_KEY")

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent = 4)
            news_json = json.loads(news)

            data = news_json

            #Access all the fiels == loop through

            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]

            final_news = []

            #loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article["content"]
                title_description = f"""
                    Title: {title},
                    Author: {author},
                    Source: {source_name},
                    Description: {description},
                    URL: {url}

                """

                final_news.append(title_description)
            return final_news
        else:
            return []

    except requests.exceptions.RequestException as e:
        print("Error occured during API Request",e)

def main():
    news = get_news("Robot")
    print (news[0])



if __name__== "__main__":
    main()