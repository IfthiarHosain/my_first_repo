import os 
from pypdf import PdfReader
pdf_path="./Resume.pdf"
try:
    reader=PdfReader(pdf_path)
    all_text=""
    for page_number,page in enumerate(reader.pages,start=1):
        text=page.extract_text()
        all_text += f"/n {page_number} ---/n {text}"
    print("extracted text from all pages", text)
    print("all text")
except FileNotFoundError:
    print(f"Error: file not found at {pdf_path} and {os.getcwd()} ")
except Exception as e :
    print(f"unexcepted error {e}") 
