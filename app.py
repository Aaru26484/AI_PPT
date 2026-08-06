import streamlit as st
import os

# Frontend
from fronted.ui import render_ui

# Backend
from backend.groq_service import generate_presentation
from backend.parser import parse_response
from backend.ppt_generator import create_presentation

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI PPT Generator",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# UI
# ----------------------------
user_data = render_ui()

# ----------------------------
# Generate Presentation
# ----------------------------
if user_data["generate"]:

    if not user_data["topic"].strip():
        st.warning("Please enter a presentation topic.")

    else:

        with st.spinner("Generating Presentation..."):

            try:

                # Generate AI response
                ai_response = generate_presentation(user_data)

                st.subheader("📄 Raw AI Response")
                st.code(ai_response, language="json")

                # Parse JSON
                presentation_data = parse_response(ai_response)

                if presentation_data is None:
                    st.error("Failed to parse AI response.")

                else:

                    # Create PPT
                    file_path = create_presentation(
                        data=presentation_data,
                        output_folder="output",
                        theme=user_data.get("theme", "Blue"),
                        font_name=user_data.get("font", "Calibri"),
                        font_size=user_data.get("font_size", 24),
                        include_images=user_data.get("include_images", True),
                        include_notes=user_data.get("speaker_notes", False)
                    )

                    st.success("✅ Presentation Generated Successfully!")

                    # Show generated file path
                    st.info(f"Saved to: {file_path}")

                    # Download button
                    if os.path.exists(file_path):

                        with open(file_path, "rb") as ppt_file:

                            st.download_button(
                                label="📥 Download Presentation",
                                data=ppt_file,
                                file_name=os.path.basename(file_path),
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            )

                    else:
                        st.error("Presentation file was not found.")

            except Exception as e:
                st.exception(e)