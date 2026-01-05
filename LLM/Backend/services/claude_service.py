from anthrpic import Anthropic
from config import Claude_API_KEY

client = Anthropic(api_key=Claude_API_KEY)

def Call_claude(prompt: str):
    client = Anthropic(api_key=Claude_API_KEY)
    response = client.chat.completions.create(
        model="claude-2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']