import streamlit as st

from langchain_ollama import ChatOllama

st.title("My Own Chat Bot! 🫡")

st.write("Much thanks to KGP Talkie on YouTube for the fantastic tutorial guiding this creation: https://youtu.be/sNSoQ7k0JFY?si=J0QgahzoPTi3yhSl")

with st.form("ollama-llm"):
    text = st.text_area("Write your prompt here: ")
    submit = st.form_submit_button("Submit.")

def generate_response(input_prompt):
    """
        This method instantiates our chosen llm.
        It then captures every prompt issued in the frontend.
        Then it returns a response.
    """
    model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")

    response = model.invoke(input_prompt)

    return response.content

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if submit and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.session_state["chat_history"].append({"user": text, "ollama": response})
        st.write(response)

st.write("--- Conversation history ---")
for chat in reversed(st.session_state["chat_history"]):
    st.write(f"** 🧔🏾 User**: {chat["user"]}")
    st.write(f"** 🤖 Assistant**: {chat["ollama"]}")
    st.write("---")

st.write("---LLAMMA 0 LAMMA OUT---")