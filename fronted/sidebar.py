import streamlit as st


def render_sidebar():

    st.sidebar.header("⚙️ Presentation Settings")

    topic = st.sidebar.text_input(
        "Presentation Topic",
        placeholder="Artificial Intelligence"
    )

    slides = st.sidebar.slider(
        "Number of Slides",
        3,
        20,
        10
    )

    style = st.sidebar.selectbox(
        "Presentation Style",
        [
            "Professional",
            "Business",
            "Educational",
            "Creative"
        ]
    )

    theme = st.sidebar.selectbox(
        "Theme",
        [
            "Blue",
            "Dark",
            "Light",
            "Green",
            "Purple"
        ]
    )

    language = st.sidebar.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Marathi"
        ]
    )

    font = st.sidebar.selectbox(
        "Font",
        [
            "Calibri",
            "Arial",
            "Times New Roman"
        ]
    )

    font_size = st.sidebar.slider(
        "Font Size",
        18,
        36,
        24
    )

    creativity = st.sidebar.slider(
        "AI Creativity",
        0.0,
        1.0,
        0.7
    )

    include_images = st.sidebar.checkbox(
        "Include Images",
        value=True
    )

    speaker_notes = st.sidebar.checkbox(
        "Generate Speaker Notes",
        value=False
    )

    generate = st.sidebar.button(
        "🚀 Generate Presentation",
        use_container_width=True
    )

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