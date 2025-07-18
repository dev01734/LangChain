
# Closed Source

'''
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

docs = [
     "Delhi is the capital of india",
     "Kolkata is the capital of west bengal",
     "Gandhinagar is the capital of gujarat" ,
     "Gandhinagar is the greenest city of india",
     "ahmedabad is cleanest city in india"
     "srinagar capital of jk",
     "Jaipur capital of RJ"
]

query = "tell me about gujarat"

doc_embeddings = embedding.embed_documents(docs)  #This embeddings are saved in DB called as Vector Database
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print("Similarity score is:", score)
'''

# -------------------------------------------------------------------------------------------------

# Open Source 

from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformers
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

docs = [
     "Delhi is the capital of india",
     "Kolkata is the capital of west bengal",
     "Gandhinagar is the capital of gujarat" ,
     "Gandhinagar is the greenest city of india",
     "ahmedabad is cleanest city in india"
     "srinagar capital of jk",
     "Jaipur capital of RJ"
]

query = "tell me about gujarat"

doc_embeddings = embedding.embed_documents(docs)  #This embeddings are saved in DB called as Vector Database
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embeddings)[0]

# print(sorted(list(enumerate(score)), key = lambda x:x[1])[-1]) #Will give the scores

index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print("Similarity score is:", score)