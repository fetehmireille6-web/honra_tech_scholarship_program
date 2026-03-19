import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()
prompt = ChatPromptTemplate.from_template("Answer this question: {question}")
chain = prompt | model | parser
response = chain.invoke({"question": "what is a large model in one paragraph?"})
print(response)