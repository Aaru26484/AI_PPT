import streamlit as st

from fronted.styles import load_css
from fronted.components import (
    show_title,
    show_subtitle,
    section_heading,
    footer
)


def render_ui():

    load_css()

    show_title()
    show_subtitle()

    st.markdown("---")

    section_heading("📊 Presentation Settings")

    col1, col2 = st.columns(2)

    with col1:

        topic = st.text_input(
            "Presentation Topic",
            placeholder="Artificial Intelligence"
        )

        slides = st.slider(
            "Number of Slides",
            3,
            20,
            10
        )

        style = st.selectbox(
            "Presentation Style",
            [
                "Professional",
                "Business",
                "Educational",
                "Creative"
            ]
        )

        theme = st.selectbox(
            "Theme",
            [
                "Blue",
                "Dark",
                "Light",
                "Green",
                "Purple"
            ]
        )

    with col2:

        language = st.selectbox(
            "Language",
            [
                "English",
                "Hindi",
                "Marathi"
            ]
        )

        font = st.selectbox(
            "Font",
            [
                "Calibri",
                "Arial",
                "Times New Roman"
            ]
        )

        font_size = st.slider(
            "Font Size",
            18,
            36,
            24
        )

        creativity = st.slider(
            "AI Creativity",
            0.0,
            1.0,
            0.7
        )

    include_images = st.checkbox(
        "Include Images",
        value=True
    )

    speaker_notes = st.checkbox(
        "Generate Speaker Notes",
        value=False
    )

    st.markdown("<br>", unsafe_allow_html=True)

    generate = st.button(
        "🚀 Generate Presentation",
        use_container_width=True
    )

    footer()

    return {
        "topic": topic,
        "slides": slides,
        "style": style,
        "theme": theme,
        "language": language,
        "font": font,
        "font_size": font_size,
        "creativity": creativity,
        "include_images": include_images,
        "speaker_notes": speaker_notes,
        "generate": generate
    }