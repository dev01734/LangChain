
# system message that we provide as - ' you are a doctor and say acordingly'

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
     SystemMessage(content='YOu are a helpful assistant'),
     HumanMessage(content='Tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)

# Using this we get to know which message is from human or from ai, so if conversation is too long 
# AI will get to know that who gave the output... 


# ====================== 