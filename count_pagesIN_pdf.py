from pypdf import PdfReader
pdf_path="./Resume.pdf"
try:
    reader= PdfReader(pdf_path)
    totall_pages=len(reader.pages)
    print("totall pages of the pdf is :", totall_pages)
except FileNotFoundError:
    print(f"Error: file don't exists in {pdf_path} please check the path or name.")
except Exception as e:
    print(" An unexpected Error occured  ", e)