import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2")

st.title("AI Interview Bot – YOUR NAME")
st.write("Ask interview questions and I’ll answer as I would.")

SYSTEM_PROMPT = """You are answering interview questions as YOUR NAME.
Speak in first person.
Tone: confident, clear, human.
Never mention being an AI.
Keep answers concise and honest.
"""

question = st.text_input("Ask an interview question")

if question:
    prompt = f"""
<system>
{SYSTEM_PROMPT}
</system>

<user>
{question}
</user>
"""

    response = client.text_generation(
        prompt,
        max_new_tokens=200,
        temperature=0.7
    )

    st.write("### My Answer")
    st.write(response)
