from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from langchain_solver import solve_question
from ocr import extract_text_from_image
import io
from PIL import Image

app = FastAPI()

# Allow extension to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
async def ocr_endpoint(screenshot: UploadFile = File(...)):
    image_bytes = await screenshot.read()
    image = Image.open(io.BytesIO(image_bytes))
    extracted_text = extract_text_from_image(image)

    # Pick first potential question
    lines = extracted_text.split('\n')
    question = next((line for line in lines if "?" in line or "=" in line), "No valid question found.")
    
    return {"question": question}

@app.post("/solve")
async def solve(payload: dict):
    question = payload.get("question", "")
    try:
        answer = solve_question(question)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}

