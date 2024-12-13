from pypdf import PdfReader, PdfWriter
pdf_path="./Resume.pdf"
pdf_path2="./job cover letter radiant.pdf"
output_path="./Merged.pdf"
try:
    writer=PdfWriter()
    pdf_path=PdfReader(pdf_path)
    for page in pdf_path.pages:
        writer.add_page(page)
    pdf_path2=PdfReader(pdf_path2)
    for page in pdf_path2.pages:
        writer.add_page(page)
    with open(output_path,"wb")as output_file:
        print("the pdfs has succesfully merged in ", output_path)
except FileNotFoundError as e:
    print(f"Error: file not found in {e} please check the path and name ")
except Exception as e:
    print(f"An unexpected error occured {e}")