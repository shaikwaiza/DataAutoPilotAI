
import streamlit as st
from google import genai

st.title("Gemini API Connection Test")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    if st.button("Test Gemini Connection"):
        with st.spinner("Connecting to Gemini..."):
            response = client.models.generate_content(
                model="gemini-3.7-flash",
                contents="Reply with: Gemini connection successful!"
            )
        st.success("Gemini responded successfully!")
        st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")
