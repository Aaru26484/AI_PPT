import os

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE


# ----------------------------------------------------
# Theme Colors
# ----------------------------------------------------

def get_theme(theme_name):

    themes = {
        "Blue": {
            "title": RGBColor(0, 51, 153),
            "body": RGBColor(40, 40, 40)
        },

        "Green": {
            "title": RGBColor(0, 128, 0),
            "body": RGBColor(40, 40, 40)
        },

        "Red": {
            "title": RGBColor(180, 0, 0),
            "body": RGBColor(40, 40, 40)
        },

        "Dark": {
            "title": RGBColor(255, 255, 255),
            "body": RGBColor(230, 230, 230)
        }
    }

    return themes.get(theme_name, themes["Blue"])


# ----------------------------------------------------
# Create Presentation
# ----------------------------------------------------

def create_presentation(
    data,
    output_folder="output",
    theme="Blue",
    font_name="Calibri",
    font_size=22,
    include_images=False,
    include_notes=False,
):

    os.makedirs(output_folder, exist_ok=True)

    prs = Presentation()

    # Standard 16:9 widescreen
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    colors = get_theme(theme)

    # ==================================================
    # TITLE SLIDE
    # ==================================================

    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)

    slide.shapes.title.text = data["title"]

    slide.placeholders[1].text = "Generated using AI PPT Generator"

    title = slide.shapes.title

    title_frame = title.text_frame
    title_frame.word_wrap = True
    title_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE

    title_para = title_frame.paragraphs[0]

    title_para.font.name = font_name
    title_para.font.size = Pt(34)
    title_para.font.bold = True
    title_para.font.color.rgb = colors["title"]
    title_para.alignment = PP_ALIGN.CENTER

    # Subtitle
    subtitle = slide.placeholders[1]

    subtitle_frame = subtitle.text_frame
    subtitle_frame.word_wrap = True
    subtitle_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE

    subtitle_para = subtitle_frame.paragraphs[0]

    subtitle_para.font.name = font_name
    subtitle_para.font.size = Pt(18)
    subtitle_para.alignment = PP_ALIGN.CENTER

    # ==================================================
    # CONTENT SLIDES
    # ==================================================

    for slide_data in data["slides"]:

        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        # -----------------------------------------
        # TITLE
        # -----------------------------------------

        title_box = slide.shapes.add_textbox(
            Inches(0.6),
            Inches(0.35),
            Inches(12.1),
            Inches(0.8)
        )

        title_frame = title_box.text_frame

        title_frame.clear()
        title_frame.word_wrap = True
        title_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE

        title_para = title_frame.paragraphs[0]

        title_para.text = slide_data["title"]

        title_para.font.name = font_name
        title_para.font.size = Pt(28)
        title_para.font.bold = True
        title_para.font.color.rgb = colors["title"]

        # -----------------------------------------
        # BODY CONTENT
        # -----------------------------------------

        body_box = slide.shapes.add_textbox(
            Inches(0.85),
            Inches(1.35),
            Inches(11.65),
            Inches(5.45)
        )

        tf = body_box.text_frame

        # Important overflow protection
        tf.clear()
        tf.word_wrap = True
        tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE

        # Keep text away from edges
        tf.margin_left = Inches(0.15)
        tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.10)
        tf.margin_bottom = Inches(0.10)

        # -----------------------------------------
        # Add bullet points
        # -----------------------------------------

        content = slide_data.get("content", [])

        for i, point in enumerate(content):

            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()

            p.text = str(point)

            # Bullet formatting
            p.level = 0

            p.font.name = font_name

            # Slightly smaller than original
            p.font.size = Pt(20)

            p.font.color.rgb = colors["body"]

            p.space_after = Pt(8)
            p.space_before = Pt(2)

            # Line spacing
            p.line_spacing = 1.05

        # -----------------------------------------
        # Speaker Notes
        # -----------------------------------------

        if include_notes:

            notes = slide_data.get("speaker_notes", "")

            if notes:

                notes_slide = slide.notes_slide

                try:
                    notes_slide.notes_text_frame.text = notes
                except Exception:
                    pass

    # ==================================================
    # SAVE PRESENTATION
    # ==================================================

    filename = (
        data["title"]
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        + ".pptx"
    )

    output_file = os.path.join(
        output_folder,
        filename
    )

    prs.save(output_file)

    # ==================================================
    # OPEN IN MICROSOFT POWERPOINT
    # ==================================================

    try:

        os.startfile(
            os.path.abspath(output_file)
        )

    except Exception as e:

        print(
            f"Could not open PowerPoint automatically: {e}"
        )

    return output_file