import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

from exercise1 import run_exercise_1
from exercise2 import run_exercise_2
from exercise3 import run_exercise_3
from exercise4 import ask_ai
from exercise5 import get_study_assistant_response

load_dotenv()
st.set_page_config(page_title="Mireille's AI Hub", layout="wide")

st.sidebar.title("Assignment navigation")
selection = st.sidebar.radio("Go to:", [
    "Exercise 1: Basic Template",
    "Exercise 2: Translator Roles",
    "Exercise 3: Simple Chain",
    "Exercise 4: Expert Function",
    "Exercise 5: Study Assistant (chat)"
])

st.title(selection)
if selection == "Exercise 1: Basic Template":
    st.header("Exercise 1: ChatPromptTemplate")
    topic = st.text_input("Enter a topic (e.g., Quantum physics):", "Artificial Intelligence")
    if st.button("Generate"):
        st.info(run_exercise_1(topic))
elif selection == "Exercise 2: Translator Roles":
    st.header("Exercise 2: System and Human Role")
    text = st.text_input("Text:", "Godd marning, how are you?")
    lang = st.text_input("Language:", "French")
    if st.button("Format Message"):
        st.write(run_exercise_2)
elif selection == "Exercise 3: Simple Chain":
    st.header("Exercise 3: Chaining with Gemini")
    q = st.text_input("Question:", "What is an LLM?")
    if st.button("Ask AI"):
        with st.spinner("Thinking......"):
            st.success(run_exercise_3(q))
elif selection == "Exercise 4: Expert Function":
    st.header("Exercise 4: Reusable Expert Function")
    role = st.selectbox("Choose Role:", ["Doctor", "Lawyer", "Engineer", "Chef"])
    q = st.text_input("Ask the expert:")
    if st.button("Consult"):
        with st.spinner("Thinking....."):
            st.write(ask_ai(role, q))
elif selection == "Exercise 5: Study Assistant (chat)":
    st.header("Exercise 5: Multi-Turn Conversation")
    if "messages" not in st.session_state:
        st.session_state.message = []
        for msg in st.session_state.message:
            role = "usre" if isinstance(msg, HumanMessage) else "assistant"
            with st.chat_message(role):
                st.write(msg.content)

        if prompt := st.chat_input("Continue our study session...."):
            st.session_state.message.append(HumanMessage(content=prompt))
            with st.chat_message("user"):
                st.write(prompt)

            with st.spinner("Assistant is thinking...."):
                response = get_study_assistant_response(prompt, st.session_state.message[:-1])
            st.session_state.message.append(AIMessage(content=response))
            with st.chat_message("assistant"):
                st.write(response)