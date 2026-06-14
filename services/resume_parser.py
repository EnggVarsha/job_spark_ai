import fitz
import pytesseract

from PIL import Image
from docx import Document
from pdf2image import convert_from_bytes

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Poppler Path
POPPLER_PATH = (
    r"C:\Users\varsha\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)


def extract_resume_text(uploaded_file):

    filename = uploaded_file.name.lower()

    try:

        # ==========================
        # PDF FILE
        # ==========================

        if filename.endswith(".pdf"):

            pdf_bytes = uploaded_file.getvalue()

            # Method 1: PyMuPDF Text Extraction

            doc = fitz.open(
                stream=pdf_bytes,
                filetype="pdf"
            )

            text = ""

            for page in doc:
                text += page.get_text()

            # If text found, return it

            if len(text.strip()) > 50:

                print("✅ PDF Text Extracted using PyMuPDF")

                return text

            # ==========================
            # Method 2: OCR Fallback
            # ==========================

            print("⚠ No text found. Running OCR...")

            images = convert_from_bytes(
                pdf_bytes,
                poppler_path=POPPLER_PATH
            )

            text = ""

            print(f"Pages Found: {len(images)}")

            for image in images:

                page_text = pytesseract.image_to_string(
                    image,
                    config="--psm 6"
                )

                text += page_text + "\n"

            print("✅ OCR Completed")

            return text

        # ==========================
        # DOCX FILE
        # ==========================

        elif filename.endswith(".docx"):

            doc = Document(uploaded_file)

            text = ""

            for para in doc.paragraphs:

                text += para.text + "\n"

            print("✅ DOCX Text Extracted")

            return text

        # ==========================
        # IMAGE FILE
        # ==========================

        elif filename.endswith(
            (".jpg", ".jpeg", ".png")
        ):

            image = Image.open(
                uploaded_file
            )

            text = pytesseract.image_to_string(
                image,
                config="--psm 6"
            )

            print("✅ Image OCR Completed")

            return text

        else:

            return "Unsupported File Type"

    except Exception as e:

        print("Resume Parser Error:", e)

        return f"Error: {str(e)}"