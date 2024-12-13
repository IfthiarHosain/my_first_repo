from pypdf import PdfReader,PdfWriter
def creat_custompdf(input_pdf1,input_pdf2,out_put_pdf):
    try:
        reader1=PdfReader(input_pdf1)
        reader2=PdfReader(input_pdf2)
        writer=PdfWriter()
        print(f"proccessing: {input_pdf1}")
        for i in range(min(2,len(reader1.pages))):
           writer.add_page(reader1.pages[i])
        print(f"proccessing: {input_pdf2}")
        total_pages_pdf2=len(reader2.pages)
        for i in range (max(0,total_pages_pdf2-2),total_pages_pdf2):
            writer.add_page(reader2.pages[i])
        with open(out_put_pdf,"wb") as output_file:
            writer.write(output_file)
        print(f"costom pdf created and saved as: {out_put_pdf}")
    except Exception as e:
        print("An unexpected Error occured ",e)
pdf_path1="./Resume.pdf"
pdf_path2="./job cover letter radiant.pdf"
out_put_pdf="./custom.pdf"
creat_custompdf(pdf_path1,pdf_path2,out_put_pdf)


