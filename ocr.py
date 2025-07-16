import pytesseract
from PIL import Image

def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

