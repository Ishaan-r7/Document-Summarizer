import streamlit as st
from producer import send_to_kafka
from consumer import get_summary

# Page config
st.set_page_config(
    page_title="Document Summarizer",
    page_icon="📄",
    layout="centered"
)

# Header
st.title("📄 Real-Time Document Summarizer")
st.write("Upload a PDF and get an AI-powered summary using Kafka and Gemini.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    st.info(f"File uploaded: {uploaded_file.name}")

    if st.button("Summarize"):
        with st.spinner("Sending to Kafka..."):
            file_bytes = uploaded_file.read()
            success = send_to_kafka(file_bytes)

        if success:
            with st.spinner("Generating summary with Gemini..."):
                summary = get_summary()

            st.success("Summary generated!")
            st.subheader("📝 Summary")
            st.write(summary)
        else:
            st.error("Failed to process PDF. Please try again.")