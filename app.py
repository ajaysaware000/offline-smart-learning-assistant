
import streamlit as st
import time
import psutil
import os

st.set_page_config(
    page_title="Offline Smart Learning Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Offline Smart Learning Assistant")

st.write(
    "An AI-powered learning assistant that generates "
    "simple summaries and quiz questions without cloud AI."
)

st.subheader("Enter Educational Passage")

passage = st.text_area(
    "Paste your educational passage here:",
    height=250,
    placeholder="Enter a passage of approximately 150–300 words..."
)

if st.button("Generate Learning Materials"):
    word_count = len(passage.split())

    if word_count < 150 or word_count > 300:
        st.warning("Please enter a passage containing 150–300 words.")

    else:
        st.info("Passage accepted. Ready for local AI processing.")

        st.write("Word count:", word_count)

        # The ExecuTorch model integration
        # will be added in the next stage.
