from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-4o", temperature=0,max_retries=3,max_completion_tokens=1024)
response=model.invoke([{"role":"user","content":"Write a poem about the sea."}])
print(response.content)