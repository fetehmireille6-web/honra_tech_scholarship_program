import streamlit as st

with st.sidebar:
    st.title("HONRAA!")
    st.write("One step at a time")
    st.divider()
    st.subheader("Session Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Messages",)
        st.subheader("1")
    with col2:
        st.subheader("Total")
        st.subheader("1")
    st.divider()
    st.subheader("Controls")
    option = st.selectbox("Accent", ("Cameroon", "Nigeria","mali", "Congo"))

    st.slider("Model Teamperature" ,min_value = 0.00, max_value = 2.00, value = 1.00)

st.header("Chat With HonraAI")
with st.container(height=350, border=True,):
    with st.chat_message("user"):
        st.write("Hello")
    with st.chat_message("assistant"):
        st.write("Hello there! I'm HonraAI, your friendly and informative assistant specializing in heart disease. I'm here to help you with questions about heart health, conditions, and riskfactors. How can i assist you today?")
        st.button("Read aloud")
st.divider()
st.chat_input("Message HonraAI")