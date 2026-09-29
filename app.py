import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Aditya Kumar Kushwaha | AI/ML Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_FILE = Path(__file__).parent / "portfolio.html"

html = HTML_FILE.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {background: #080b14;}
        .block-container {
            padding-top: 0;
            padding-bottom: 0;
            max-width: 100%;
        }
        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.components.v1.html(
    html,
    height=2600,
    scrolling=True,
)
