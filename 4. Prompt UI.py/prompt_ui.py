
'''
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

user_input = st.tect_input('Enter Your Prompt')

if st.button:
     st.text('Some random text')
'''


# ----------------

from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model= ChatHuggingFace(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
st.header('Research Tool')

user_input = st.tect_input('Enter Your Prompt')

if st.button('summarize'):
     result = model.invoke(user_input)
     st.text('Some random text')