from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found! Check your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Test API call
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What is AI?"}
    ]
)

# Print response
print(completion.choices[0].message.content)


