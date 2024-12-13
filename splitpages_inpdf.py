from pypdf import PdfReader , PdfWriter
import os
pdf_path="./Resume.pdf"
output_path="./splitpages"
os.makedirs(output_path,exist_ok=True)
try:
    reader=PdfReader(pdf_path)
    for page_number,page in enumerate(reader.pages,start=1):
        writer=PdfWriter()
        writer.add_page(page)
        output_file=os.path.join(output_path,f"page{page_number}.pdf")
        with open(output_file,"wb") as output_pdf:
            writer.write(output_pdf)
        print(f"saved file {output_file}")
    print(f"successfully split the pdf into {len(reader.pages)} pages")
except FileNotFoundError:
    print("Error: the file isn't in: ", pdf_path)
except Exception as e:
    print("An Unexpected Error occured: ", e)
