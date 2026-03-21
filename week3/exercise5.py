import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def get_study_assistant_response(user_input, history):
    load_dotenv()
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
    parser = StrOutputParser()
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful study assistant."),
        MessagesPlaceholder(variable_name="history"),("human", "{input}")
    ])
    chain = chat_prompt | model | parser
    return chain.invoke({"history": history, "input": user_input})
