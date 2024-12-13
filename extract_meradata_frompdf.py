from pypdf import PdfReader
pdf_path="./Resume.pdf"
try:
    reader=PdfReader(pdf_path)
    meta_data=reader.metadata
    if meta_data:
        print("Pdfs metadata:")
        for key in meta_data:
            value= meta_data[key]
            print(f"{key}: {value}")
        else:
            print("no metadata found")
except FileNotFoundError:
    print("Error: file is not found in", {pdf_path})
except Exception as e:
    print("An Unexpected Error occured", e)