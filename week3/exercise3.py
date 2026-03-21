import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def run_exercise_3(question):
    load_dotenv()
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
    parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_template("Answer this question: {question}")
    chain = prompt | model | parser
    return chain.invoke({"question": question})