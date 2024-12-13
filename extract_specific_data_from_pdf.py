import re
from pypdf import PdfReader
def extract_emails_and_phonenumbers(pdf_path):
    try:
        reader= PdfReader(pdf_path)
        text=""
        for page in reader.pages:
            text +=page.extract_text()
        email_pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_number_pattern=r'\b\d{10}\b|\b(?:\d{3}-\d{3}-\d{4})\b|\b\(\d{3}\)\s?\d{3}-\d{4}\b'
        emails=re.findall(email_pattern,text)
        phone_numbers=re.findall(phone_number_pattern,text)
        return emails,phone_numbers
    except Exception as e:
        print("An unexpected Error occured:", e)
        return[],[]
pdf_path="./Resume.pdf"
emails,phone_numbers=extract_emails_and_phonenumbers(pdf_path)
print("Emails found: ", emails)
print("phone_numbers found: ", phone_numbers)
