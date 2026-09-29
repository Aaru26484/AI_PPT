from groq import Groq

from config.settings import GROQ_API_KEY
from backend.prompt_builder import build_prompt

# Use the new Groq model
MODEL_NAME = "openai/gpt-oss-120b"

client = Groq(
    api_key=GROQ_API_KEY
)


def generate_presentation(user_data):

    print("MODEL BEING USED:", MODEL_NAME)

    prompt = build_prompt(user_data)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert AI presentation creator. "
                        "Always return valid JSON only."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=user_data["creativity"],
            max_tokens=8192
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"Groq API Error: {e}")