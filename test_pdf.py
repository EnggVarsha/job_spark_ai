import fitz

pdf_path = "Resume Varsha Samal.pdf"

doc = fitz.open(pdf_path)

for page in doc:
    text = page.get_text()
    print(text[:1000])