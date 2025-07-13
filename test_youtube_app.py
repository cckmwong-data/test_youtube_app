import streamlit as st

# Title of the app
st.title("Open YouTube in Streamlit")

# Embed the YouTube homepage
youtube_url = "https://www.youtube.com"
st.components.v1.iframe(youtube_url, width=1000, height=600)