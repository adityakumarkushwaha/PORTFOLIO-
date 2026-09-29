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

# Compact spacing CSS
compact_css = """
<style>
/* ===== COMPACT PORTFOLIO SPACING ===== */

/* Hero section */
.hero {
    min-height: 70vh !important;
    padding-top: 45px !important;
    padding-bottom: 35px !important;
}

/* All main sections */
section {
    padding-top: 50px !important;
    padding-bottom: 50px !important;
}

/* Section headings */
.section-head {
    margin-bottom: 25px !important;
}

/* Reduce common large gaps */
.about,
.skills,
.projects,
.education,
.contact {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

/* Cards/grid spacing */
.project-grid,
.skills-grid,
.education-grid {
    gap: 25px !important;
}

/* Mobile */
@media (max-width: 850px) {

    .hero {
        min-height: auto !important;
        padding-top: 50px !important;
        padding-bottom: 35px !important;
    }

    section {
        padding-top: 40px !important;
        padding-bottom: 40px !important;
    }

    .section-head {
        margin-bottom: 20px !important;
    }
}
</style>
"""

# Inject CSS into portfolio HTML
if "</head>" in html:
    html = html.replace(
        "</head>",
        compact_css + "\n</head>"
    )
else:
    html = compact_css + html


# Hide Streamlit default UI
st.markdown(
    """
    <style>
        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        .stApp {
            background: #080b14;
        }

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


# Display portfolio
st.components.v1.html(
    html,
    height=2200,
    scrolling=True,
)
