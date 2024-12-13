from pypdf import PdfReader, PdfWriter
import os
import logging
logging.basicConfig(level=logging.INFO)
pdf_path="./job cover letter radiant.pdf"
output_path="./"
try:
    logging.info("starting the script...")
    reader=PdfReader(pdf_path)
    writer=PdfWriter()
    for page in reader.pages:
        page.rotate(90)
        writer.add_page(page)
    output_dir=os.path.dirname(output_path)
    os.makedirs(output_dir,exist_ok=True)
    with open(output_path,"wb") as output_file:
        writer.write(output_file)
    logging.info(f"the pdf has rotate and saved as:", output_path)

except FileNotFoundError:
    print(f"Error: the file isn't in {pdf_path}")
except Exception as e:
    print("An unexpected Error occured:",e)






        