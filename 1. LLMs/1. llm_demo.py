# from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-flash")

ans = llm.invoke("What is capital India?")

print(ans)

# =================================

# from langchain_google_genai import GoogleGenerativeAI