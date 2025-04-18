import fitz
import pytesseract
from PIL import Image
import io

def extract_text_and_images_from_pdf(filepath):
    doc = fitz.open(filepath)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

        images = page.get_images(full=True)
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))

            ocr_text = pytesseract.image_to_string(image)
            if ocr_text.strip():
                full_text += f"\n[Image OCR Text]: {ocr_text}\n"

    return full_text
