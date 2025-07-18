# Closed Source
# Open AI

# temperature lies 0 - 2, if kept temperature ~0  will always give almost similar output, ~1.5 will give new everytime

'''
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0.3, max_completion_tokens=50) #temperature is it will be more creative or deterministic
result = model.invoke("What is India?")                     #max_completion_tokens is how many token it will return from LLM, tokens = words
print(result)
'''

# ------------------------------------------------------------------------------

# Claude
'''
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model = "claude-3-5-haiku-latest")
result = model.invoke("india capital")
print(result)
'''

# ------------------------------------------------------------------------------

# Gemini
'''
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
result = model.invoke("india capital")
print(result)
'''

# ------------------------------------------------------------------------------

