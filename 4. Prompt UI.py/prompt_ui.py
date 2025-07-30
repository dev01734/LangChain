
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

# Gemini API
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt # load_prompt to import template from some other file

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

st.header('Research Tool')

paper_input = st.selectbox("select Research paper", ['Attention is all you need', 'BERT: Pre training of deep bidirectional transformer', 'GPT-3 model are few shot learning'])

style_input = st.selectbox('Select Explanation Style', ['Begineer Freindly', 'Technical', 'Academic'])

length_input = st.selectbox('Select Length', ['Short', 'Medium', 'Long'])

#template : instead of using these here we can create a file where we can import from there

template = load_prompt("template.json") #can call this directly instead of writing full template code
'''
template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
        - Include relevent math equations if present in paper.
        - Explain mathematical concepts using simple, intuative code snippets where applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex concepts.
    IF certain info is not available in paper, respond with "insufficient infor" instead of guessing.
    Ensure the summary is clear, accurate and aligned with provided style and length.
""",
input_variables = ['paper_input', 'style_input', 'length_input'],
validate_template= True  # Checks if all the inputs are also in input_variable isn't there and less or more
)
'''

#fill placeholders
prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)


# ----------------
# Open Source Model - when using open source model, we need to use the pipeline function to load the model and the transformer

# '''
# import streamlit as st
# from langchain_huggingface import ChatHuggingFace
# from langchain_huggingface.llms import HuggingFacePipeline
# from transformers import pipeline

# # Load model via Hugging Face transformers
# hf_pipeline = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device=-1) #device = -1 if cpu not avialble

# # Wrap the HF pipeline with LangChain wrapper
# wrapped_llm = HuggingFacePipeline(pipeline=hf_pipeline)

# # Use wrapped LLM in ChatHuggingFace
# chat_model = ChatHuggingFace(llm=wrapped_llm)

# # Streamlit UI
# st.header('Research Tool')
# user_input = st.text_input('Enter Your Prompt')

# if st.button('Summarize') and user_input:
#     result = chat_model.invoke(user_input)
#     st.text(result)
# '''


