def build_prompt(data):

    topic = data["topic"]
    slides = data["slides"]
    style = data["style"]
    theme = data["theme"]
    language = data["language"]
    font = data["font"]
    font_size = data["font_size"]
    speaker_notes = data["speaker_notes"]

    prompt = f"""
You are a world-class presentation designer, technical writer, and subject matter expert.

Create a professional Microsoft PowerPoint presentation.

Presentation Details:
- Topic: {topic}
- Number of Slides: {slides}
- Style: {style}
- Theme: {theme}
- Language: {language}
- Font: {font}
- Font Size: {font_size}

IMPORTANT CONTENT RULES:

1. Generate EXACTLY {slides} slides.

2. Organize the presentation logically.

3. Every slide MUST contain:
   - One professional slide title.
   - EXACTLY 5 bullet points.
   - Each bullet must be SHORT and presentation-friendly.
   - Each bullet should contain approximately 8–14 words.
   - Never write long paragraphs.
   - Never combine multiple ideas into one bullet.
   - Each bullet should communicate one clear idea.
   - Do not repeat the slide title inside the bullets.
   - Avoid unnecessary explanations.
   - Avoid filler words.
   - Keep all content concise enough to fit on one PowerPoint slide.

4. Content should:
   - Be suitable for college, technical, and business presentations.
   - Use professional and simple language.
   - Be informative but concise.
   - Cover different aspects of the topic on different slides.
   - Use keywords where appropriate.
   - Prefer short phrases and clear sentences.

5. IMPORTANT:
   - NEVER generate large paragraphs.
   - NEVER generate more than 14 words in a single bullet.
   - NEVER generate more than 5 bullets per slide.
   - Keep slide content visually clean.
   - Content must fit comfortably inside a standard 16:9 PowerPoint slide.

6. Do NOT include:
   - Markdown
   - Tables
   - Code
   - Numbered lists
   - Image keywords
   - Image filenames
   - Extra explanations outside JSON

7. Speaker Notes:
"""

    if speaker_notes:
        prompt += """
Generate 2–3 short and informative sentences as speaker notes for each slide.
Speaker notes can contain additional explanation that does not need to appear on the slide.
"""
    else:
        prompt += """
Leave speaker_notes as an empty string.
"""

    prompt += """

Return ONLY valid JSON.

Use exactly this format:

{
    "title": "Presentation Title",
    "slides": [
        {
            "title": "Slide Title",
            "content": [
                "Short bullet point about the topic",
                "Another concise and informative point",
                "Important concept explained briefly",
                "Useful information about the topic",
                "Final key point for this slide"
            ],
            "speaker_notes": ""
        }
    ]
}
"""

    return prompt