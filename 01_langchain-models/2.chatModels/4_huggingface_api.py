from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()   

llm=HuggingFaceEndpoint(
    repo_id="TinyLLM/tinyllm-7b-chat",
    task="text-generation",
    model_kwargs={"temperature":0,"max_new_tokens":1024},
)

model=ChatHuggingFace(llm=llm)
response=model.invoke([{"role":"user","content":"what is the capital of pakistan?"}
    ])  
print(response.content)