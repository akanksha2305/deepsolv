import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "task1/data/pdfs/Apple_Vision_Pro_Privacy_Overview.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    with open("task1/data/pdfs/extracted_text.txt", "w") as file:
        file.write(extracted_text)
