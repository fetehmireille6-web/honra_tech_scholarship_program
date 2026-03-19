import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful study assistant."),
    MessagesPlaceholder(variable_name="history"),("human", "{input}")
])
chain = chat_prompt | model | parser
history = []
input1 = "Hi, I'm Mireille. I'm studying computer Engineering."
resp1 = chain.invoke({"history": history, "input": input1})
history.append(("human", input1))
history.append(("ai", resp1))
print(f"\nAI (Turn 1): {resp1}")

input2 = "What is the most important subject in my field?"
resp2 = chain.invoke({"history": history, "input": input2})
history.append(("human", input2))
history.append(("ai", resp2))
print(f"\nAI (Turn 2): {resp2}")

input3 = "Can you suggest a project idea for it?"
resp3 = chain.invoke({"history": history, "input": input3})
print(f"\nAI (Turn 3 - Memory Test): {resp3}")

