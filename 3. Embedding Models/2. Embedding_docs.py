
# Closed Source
# Open AI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

documents = [
     "Delhi is the capital of india",
     "Kolkata is the capital of west bengal",
     "Gandhinagar is the capital of gujarat"
]

result = embedding.embed_documents(documents)
print(str(result))

# ----------------------------------------------------------------------------------

# Open Source 

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
     "Delhi is the capital of india",
     "Kolkata is the capital of west bengal",
     "Gandhinagar is the capital of gujarat"
]

vector = embedding.embed_documents(documents)

print(str(vector))