import os
from pypdf import PdfReader
pdf_path="./Merged.pdf"
if not os.path.exists(pdf_path):
    print(f"Error: file {pdf_path} not found in {os.getcwd()}")
else:
    reader=PdfReader(pdf_path)
    frist_page=reader.pages[0]
    text=frist_page.extract_text()
    print("text from the pages")
    print(text)