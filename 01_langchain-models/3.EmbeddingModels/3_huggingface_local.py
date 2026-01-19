from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=["Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million. Islamabad is the capital city of Pakistan.","The capital of Pakistan is Islamabad. It is known for its high standard of living, safety, and abundant greenery. The city was built during the 1960s to replace Karachi as Pakistan's capital."]

result = embeddings.embed_documents(documents)

print(str(result))