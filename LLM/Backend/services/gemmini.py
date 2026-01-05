import google.generativeai as genai
from config import Claude_API_KEY
genai.configure(api_key=Claude_API_KEY)
def Call_gemmini(prompt: str):
    response = genai.chat.completions.create(
        model="gemini-1.5-pro",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.candidates[0].content