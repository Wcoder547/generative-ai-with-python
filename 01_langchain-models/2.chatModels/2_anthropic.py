from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model=ChatAnthropic(model="claude-2", temperature=0, max_retries=3, max_completion_tokens=1024)
response=model.invoke([{"role":"user","content":"Write a poem about the sea."}  ])
print(response.content)