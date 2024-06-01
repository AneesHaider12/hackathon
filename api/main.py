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
    suggestion = get_openai_suggestion(prompt, style, image_url)
    return {"suggestion": suggestion}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")






