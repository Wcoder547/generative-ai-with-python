from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

documents=["Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million. Islamabad is the capital city of Pakistan.","The capital of Pakistan is Islamabad. It is known for its high standard of living, safety, and abundant greenery. The city was built during the 1960s to replace Karachi as Pakistan's capital."]
result=embedding.embed_documents(documents)
print(str(result))
