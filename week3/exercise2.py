import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def run_exercise_2(text, language):
    load_dotenv()
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
    parser = StrOutputParser()
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a professional translator."),
        ("human", "Translate '{text}' into {language}.")
    ])
    return prompt_template.format_messages(text=text, language=language)