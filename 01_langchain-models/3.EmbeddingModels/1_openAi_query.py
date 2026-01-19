from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddingsModel=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
result=embeddingsModel.embed_query("What is the capital of Pakistan?")
print(str(result))  