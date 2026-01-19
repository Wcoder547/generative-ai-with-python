from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

import os
os.environ["HF_HOME"] = "D:/IMPORTANT MEGA/AI/HuggingFace"

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
        pipeline_kwargs={"max_new_tokens":1024, "temperature":0}
    
)    
model=ChatHuggingFace(llm=llm)
response=model.invoke([{"role":"user","content":"what is the capital of pakistan?"}
    ])

print(response.content)
