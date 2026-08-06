import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


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

    title_para = title.text_frame.paragraphs[0]
    title_para.font.name = font_name
    title_para.font.size = Pt(34)
    title_para.font.bold = True
    title_para.font.color.rgb = colors["title"]
    title_para.alignment = PP_ALIGN.CENTER

    # ==================================================
    # CONTENT SLIDES
    # ==================================================

    for slide_data in data["slides"]:

        slide_layout = prs.slide_layouts[6]  # Blank Layout
        slide = prs.slides.add_slide(slide_layout)

        # -----------------------------------------
        # Title
        # -----------------------------------------

        title_box = slide.shapes.add_textbox(
            Inches(0.6),
            Inches(0.4),
            Inches(12),
            Inches(0.8)
        )

        title_frame = title_box.text_frame

        title_para = title_frame.paragraphs[0]

        title_para.text = slide_data["title"]

        title_para.font.name = font_name
        title_para.font.size = Pt(28)
        title_para.font.bold = True
        title_para.font.color.rgb = colors["title"]

        # -----------------------------------------
        # Bullet Content (Centered)
        # -----------------------------------------

        body_box = slide.shapes.add_textbox(
            Inches(1.0),
            Inches(1.5),
            Inches(11.3),
            Inches(4.8)
        )

        tf = body_box.text_frame
        tf.clear()

        for i, point in enumerate(slide_data["content"]):

            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()

            p.text = point
            p.level = 0

            p.font.name = font_name
            p.font.size = Pt(font_size)
            p.font.color.rgb = colors["body"]

            p.space_after = Pt(10)
            p.space_before = Pt(3)

        # -----------------------------------------
        # Speaker Notes
        # -----------------------------------------

        if include_notes:

            notes = slide_data.get("speaker_notes", "")

            if notes:

                notes_slide = slide.notes_slide
                notes_slide.notes_text_frame.text = notes

    # ==================================================
    # Save Presentation
    # ==================================================

    filename = (
        data["title"]
        .replace(" ", "_")
        .replace("/", "_")
        + ".pptx"
    )

    output_file = os.path.join(output_folder, filename)

    prs.save(output_file)

    # ==================================================
    # Open in Microsoft PowerPoint
    # ==================================================

    try:
        os.startfile(os.path.abspath(output_file))
    except Exception as e:
        print(f"Could not open PowerPoint automatically: {e}")

    return output_file