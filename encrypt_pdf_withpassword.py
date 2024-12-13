from pypdf import PdfReader,PdfWriter
def encrypt_pdf(input_pdf_path,output_pdf_path,password):
    try:
        reader=PdfReader(input_pdf_path)
        writer=PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with open(output_pdf_path,"wb") as output_file:
            writer.write(output_file)
        print("pdf has been encryted and saved as: ",output_pdf_path)
    except Exception as e:
        print("An unexpected Error occured: ",e)
input_pdf_path="./Resume.pdf"
output_pdf_path="./encryted.pdf"
password="secure"
encrypt_pdf(input_pdf_path,output_pdf_path,password)
