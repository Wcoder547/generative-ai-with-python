from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv", encoding="utf-8")

docs = loader.load()

print(f"Loaded {len(docs)} documents.")