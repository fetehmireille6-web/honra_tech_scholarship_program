import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def run_exercise_1(topic):
    load_dotenv()
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
    parser = StrOutputParser()

    template = "Explain {topic} as if i am a complete beginer."
    prompt_template = ChatPromptTemplate.from_template(template)
    return prompt_template.format_messages(topic=topic)