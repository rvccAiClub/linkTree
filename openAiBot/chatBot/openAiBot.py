import os
from dotenv import load_dotenv
import openai


# Load environment variables
load_dotenv()

# Get openAi key
openai.api_key = os.getenv('API_KEY')
