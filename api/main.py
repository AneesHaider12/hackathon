from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import Annotated
import base64

from utils import get_openai_suggestion

app = FastAPI()


@app.get("/")
def health_check(): 
    return {"status": "ok"}



@app.post("/get_openai_answer") 
async def get_openai_answer(prompt: str, style: str , image : UploadFile ): 
    if image.content_type not in ["image/jpeg", "image/png", "image/gif"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG, PNG, and GIF files are allowed.")
    
    contents = await image.read()
    base64_image = base64.b64encode(contents).decode('utf-8')
    image_url = f"data:image/jpeg;base64,{base64_image}"
    # suggestion = get_openai_suggestion(prompt, style, image_url)
    suggestion = """To create a historical and stylized room with the existing space shown in the image, you can follow these guidelines:\n\n### Wall Treatment\n1. **Paint and Wallpaper:**\n   - Wallpaper with intricate historical patterns, such as damask or toile de Jouy, can add a rich historical touch.\n   - If you prefer paint, consider deep, classic colors like burgundy, forest green, or royal blue, often seen in historical rooms.\n\n2. **Wainscoting and Moldings:**\n   - Install wainscoting on the lower half or third of the wall and crown moldings around the ceiling. These architectural details are key in historical decor.\n\n### Flooring\n1. **Rugs:**\n   - Lay down a richly patterned Persian or Oriental rug in the center of the room to add warmth and a historical element.\n\n### Furniture\n1. **Antique-style Furniture:**\n   - Choose furniture pieces with ornate carvings and rich wood tones. Pieces like a vintage loveseat, armchairs with carved arms, and an elegant wooden coffee table with clawfoot legs can evoke historical elegance.\n\n2. **Bookshelves and Cabinets:**\n   - Add bookshelves or glass-fronted cabinets with intricate detailing to display antique books, collectibles, or other historical artifacts.\n\n### Lighting\n1. **Chandeliers and Sconces:**\n   - Install a crystal chandelier or a brass chandelier with candles to create a focal point. Antique wall sconces on either side of the room will"""
    return {"suggestion": suggestion}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")






