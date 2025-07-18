
# Closed Source
# Open AI
'''
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)
result = embedding.embed_query("Delhi is capital of india")
print(str(result))
'''

#----------------------------------------------------------------------------------------

# Open Source

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = "delhi capital of india"

vector = embedding.embed_query(text)

print(str(vector))