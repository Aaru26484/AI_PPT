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

Instructions:

1. Generate EXACTLY {slides} slides.

2. Organize the presentation logically using sections such as:
   - Introduction
   - Background
   - Definition
   - Key Concepts
   - Working Process
   - Features
   - Advantages
   - Challenges
   - Applications
   - Future Scope
   - Conclusion

3. Every slide MUST contain:
   - One professional slide title.
   - EXACTLY 6 bullet points.
   - Every bullet must start directly with the content (do not use numbering).
   - Every bullet must be a complete sentence.
   - Every bullet must contain between 18 and 25 words.
   - Every bullet should explain one important concept.
   - Every bullet should be informative and presentation-ready.
   - Avoid one-word bullets.
   - Avoid repeating information across slides.

4. The content should:
   - Be suitable for college, technical, and business presentations.
   - Use professional English.
   - Be concise but meaningful.
   - Cover different aspects of the topic on every slide.

5. Do NOT include:
   - Markdown
   - Tables
   - Code
   - Numbered lists
   - Image keywords
   - Image filenames
   - Extra explanations outside JSON

6. Speaker Notes:
"""

    if speaker_notes:
        prompt += """
Generate 2–3 informative speaker notes for each slide.
"""
    else:
        prompt += """
Leave speaker_notes as an empty string.
"""

    prompt += """

Return ONLY valid JSON in the following format:

{
    "title": "Presentation Title",
    "slides": [
        {
            "title": "Slide Title",
            "content": [
                "Bullet point one with detailed information.",
                "Bullet point two with detailed information.",
                "Bullet point three with detailed information.",
                "Bullet point four with detailed information.",
                "Bullet point five with detailed information.",
                "Bullet point six with detailed information."
            ],
            "speaker_notes": ""
        }
    ]
}
"""

    return prompt