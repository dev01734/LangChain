from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.0-flash')

chat_history = [
     SystemMessage(content="You are helpful ai assistant")
]
while True:
     user_input= input("You: ")
     chat_history.append(HumanMessage(content=user_input))
     if user_input == 'exit':
          break
     result = model.invoke(chat_history)
     chat_history.append(AIMessage(content=result.content))
     print ("AI: ", result.content)
print(chat_history)