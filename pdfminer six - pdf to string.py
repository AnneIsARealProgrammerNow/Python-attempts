#taken from: http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php
from io import StringIO #modified from source to run with Python 3.6
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt, io

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb') #changed from original, which used 'file'
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1] 
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
#            textFilename = txtDir + pdf.split(".")[0] + ".txt"
#            textFile = open(textFilename, "w") #make text file
            with io.open( pdf.split(".")[0] + "v2.txt", 'w', encoding='utf-8') as file:
                 file.write(text)

pdfDir = "D:\Documents sync\Google Drive\Graz\AA thesis\Python attempts\pdfs\\"
txtDir = "D:\Documents sync\Google Drive\Graz\AA thesis\Python attempts\txts\\"
convertMultiple(pdfDir, txtDir)