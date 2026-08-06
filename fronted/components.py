import streamlit as st


def show_title():

    st.markdown(
        """
        <div class="main-title">
            📊 AI PPT Generator
        </div>
        """,
        unsafe_allow_html=True
    )


def show_subtitle():

    st.markdown(
        """
        <div class="sub-title">
            Generate Professional PowerPoint Presentations using Groq AI
        </div>
        """,
        unsafe_allow_html=True
    )


def section_heading(title):

    st.markdown(
        f"""
        <h3 style="color:#2563EB;">
            {title}
        </h3>
        """,
        unsafe_allow_html=True
    )


def footer():

    st.markdown(
        """
        <hr>

        <div class="footer">

        Developed using ❤️ Streamlit + Groq API

        </div>
        """,
        unsafe_allow_html=True
    )