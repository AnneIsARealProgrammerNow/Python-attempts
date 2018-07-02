#gives txt file as output

import PyPDF2

pdf_name = 'andorra-bur2.pdf'

with open(pdf_name,'rb') as pdf_file, open('sample.txt', 'w') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)
        
open(pdf_name, 'rb')