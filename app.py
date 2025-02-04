import streamlit as st
import asyncio
import os
import time
#from main import generate_report, podcast_from_report

# Set Streamlit Page Configurations
st.set_page_config(page_title="AI Report Generator", layout="wide")

# Sidebar - User Inputs
st.sidebar.header("Report Configuration")
report_topic = st.sidebar.text_area("Report Topic", "Give an overview of capabilities and specific use case examples for these processing units: CPU, GPU.")
number_of_queries = st.sidebar.number_input("Number of Queries per Section", min_value=1, max_value=5, value=2)
tavily_topic = "general"
tavily_days = None

# Load previously saved report 
report_file_path = "final_report.md"
if os.path.exists(report_file_path):
    with open(report_file_path, "r", encoding="utf-8") as file:
        saved_report = file.read()
else:
    saved_report = None

# Generate Report Button
if st.sidebar.button("Generate Report"):
    sidebar_placeholder = st.sidebar.empty() 
    sidebar_placeholder.text("Generating report...") 

    with st.spinner("Generating report..."):
        report = asyncio.run(generate_report(report_topic, number_of_queries))
        report = {"final_report": saved_report} 
        st.session_state["report"] = report  

    sidebar_placeholder.text("")
    st.sidebar.success("Report generation successful!")

# Display Final Report
if "report" in st.session_state:
    st.subheader("Generated Report")
    st.markdown(st.session_state["report"]["final_report"], unsafe_allow_html=True)
    
    # Download Report Button
    st.download_button(label="Download Report", data=st.session_state["report"]["final_report"], file_name="report.md")

# Podcast Conversion 
st.sidebar.header("Podcast Conversion")
voice_options = {
    "Male": "29vD33N1CtxCmqQRPOHJ",  
    "Female": "21m00Tcm4TlvDq8ikWAM"  
}
voice_choice = st.sidebar.radio("Select Voice", list(voice_options.keys()))
voice_id = voice_options[voice_choice]

language_options = {"English": "en", "French": "fr", "Spanish": "es", "Hindi": "hi", "Arabic": "ar", "Japanese": "ja"}
language = st.sidebar.selectbox("Select Language", list(language_options.keys()))
selected_language_code = language_options[language]
duration = st.sidebar.slider("Select Duration (Minutes)", min_value=1, max_value=10, value=3)

if st.sidebar.button("Generate Podcast"):
    sidebar_placeholder = st.sidebar.empty() 
    sidebar_placeholder.text("Generating podcast...") 

    with st.spinner("Generating podcast audio..."): 
        asyncio.run(podcast_from_report(voice=voice_id, language=selected_language_code, duration=duration))
    
    sidebar_placeholder.text("")
    st.sidebar.success("Podcast generated! Play or download below.")
    
    # Provide download link and audio player
    audio_path = "speech_script_el.mp3"
    if os.path.exists(audio_path):
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.sidebar.audio(audio_bytes, format="audio/mp3", start_time=0, autoplay=True)
            st.sidebar.download_button(label="Download Podcast", data=audio_bytes, file_name="report_podcast.mp3", mime="audio/mpeg")
