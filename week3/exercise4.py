import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

def ask_ai(role, question):
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a professional {role}."),("human", "{question}")
    ])
    chain = prompt | model | parser
    return chain.invoke({"question": question})
print(f"Doctor: {ask_ai('Doctor', 'What are the symptoms of malaria?')}")
print(f"Lawyer: {ask_ai('Lawyer', 'What is a non-dislosure agreement?')}")
print(f"Engineer: {ask_ai('Engineer', 'What is the OSI model?')}")