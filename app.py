import streamlit as st
from openai import OpenAI
import tempfile

client = OpenAI()

st.title("AI Interview Voice Bot – NAGA LAKSHMI")
st.write("Click record, ask an interview question, and hear my answer.")

audio = st.audio_input("Record your question")

SYSTEM_PROMPT =

if audio:
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(audio.read())
        audio_path = f.name

    transcript = client.audio.transcriptions.create(
        file=open(audio_path, "rb"),
        model="whisper-1"
    )

    question = transcript.text
    st.write("You asked:", question)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    st.write("My answer:", answer)

    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=answer
    )

    st.audio(speech.read(), format="audio/mp3")
