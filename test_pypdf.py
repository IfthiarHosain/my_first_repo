from pypdf import PdfReader
pdf_path="C:\Users\pc\OneDrive\Desktop\programing\learncode.py\Resume.pdf"
reader=PdfReader("C:\Users\pc\OneDrive\Desktop\programing\learncode.py\Resume.pdf")
for page in reader:
    print(page.extract_txt())
