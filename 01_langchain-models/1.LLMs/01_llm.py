from dotenv import load_dotenv
from langchain_perplexity import ChatPerplexity

load_dotenv()

model = ChatPerplexity(model="sonar-pro", temperature=0.7)

# response = model.invoke("What is LangChain?")
# print(response.content)
messages=[{"role":"user","content":"Write a poem about AI"}]

for chunk in model.stream(messages):
    print(chunk.content)
