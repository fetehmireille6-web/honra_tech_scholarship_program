import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


def ask_ai(role, question):
    load_dotenv()
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
    parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a professional {role}."),("human", "{question}")
    ])
    chain = prompt | model | parser
    return chain.invoke({"question": question})
