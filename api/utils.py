from openai import OpenAI 
from config import OPENAI_API_KEY

client = OpenAI(api_key = OPENAI_API_KEY)

def get_openai_suggestion(prompt: str, style: str, image_url: str):
    BASE_PROMPT = f"""You are room decoration expert. You have to give advice to user on the room decoration. 
    The user has uploaded an image of the room. You have to give advice to the user on how to decorate the room.
    
    The style user wants is {style}. 

    Additional requirements from users are {prompt}.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": BASE_PROMPT,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                },
                },
            ],
            }
        ],
        )

    return response.choices[0].message.content 