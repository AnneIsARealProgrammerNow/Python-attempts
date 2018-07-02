#reads pdf to string, removes white spaces, writes to txt

#set the input and output here
name = 'mongolia-bur1'

pdf_name = name + '.pdf'
txt_name = name + '.txt'

import PyPDF2

#read the pdf using PyPDF2
pdfFileObj = open(pdf_name,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

#remove white spaces    
text_join = "".join(text.splitlines())

#write to txt file (overwrites)
Txt_join = open(txt_name, 'w', encoding='utf-8')
Txt_join.write(text_join)
