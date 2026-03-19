import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator."),
    ("human", "Translate '{text}' into {language}.")
])
french_result = prompt_template.format_messages(text = "Good morning, how are you?", language="French")
print(f"French prompt:  {french_result}")

pidgin_result = prompt_template.format_messages(text="Good morning, how are you?", language = "Cameroon Pidgin English")
print(f"Pidgin Prompt: {pidgin_result}")