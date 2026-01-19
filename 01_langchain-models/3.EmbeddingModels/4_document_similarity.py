from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents=["Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million. Islamabad is the capital city of Pakistan.","The capital of Pakistan is Islamabad. It is known for its high standard of living, safety, and abundant greenery. The city was built during the 1960s to replace Karachi as Pakistan's capital."]

query="What is the capital of Pakistan?"

doc_embeeding = embeddings.embed_documents(documents)

query_embedding = embeddings.embed_query(query)


scores = cosine_similarity([query_embedding], doc_embeeding)[0]

print("Similarity Scores:", scores)


index,score=sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)

print(f"Most similar document is at index {index} with a similarity score of {score}")
print("Document:", documents[index])
print("Embedding:", doc_embeeding[index])
print("similarity score:", score)


# Most similar document is at index 1 with a similarity score of 0.91
# Document: The capital of Pakistan is Islamabad...
# Embedding: [0.23, -0.12, 0.91, ...]
# similarity score: 0.91
