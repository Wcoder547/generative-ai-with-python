from langchain_google_genai import ChatGoogleGemini
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGemini(model="gemini-1.5-pro", temperature=0, max_retries=3, max_completion_tokens=1024)
response = model.invoke([{"role": "user", "content": "Write a poem about the sea."}])
print(response.content)