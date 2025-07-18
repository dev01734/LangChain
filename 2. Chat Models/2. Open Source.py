# Open Source
# Hugging Face using api from hugging face
'''
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
     repo_id= "HuggingFaceH4/zephyr-7b-beta",
     task = "text-generation"
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("what is india")
print(result.content)
'''

# --------------------------------------------------------------------

# Hugging face but download model locally on pc

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache' #if this not written will auto download to C:/ drive
llm = HuggingFacePipeline.from_model_id(
     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
     task= "text-generation",
     pipeline_kwargs=dict(
          temperature = 0.5,
          max_new_tokens = 100
     )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of india")
print(result.content)
