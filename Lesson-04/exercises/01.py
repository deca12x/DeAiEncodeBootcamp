import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
 {
      "role": "user",
      "content": "What is the capital of France?"
 }
]
)

print(completion.choices[0].message.content);
