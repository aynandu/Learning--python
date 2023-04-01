import PyPDF2       #this a PyPDF2 v1.26 , syntax may be different from current
import sys
'''

with open('dummy.pdf','rb') as file:  #rb means read binary
    reader=PyPDF2.PdfFileReader(file)
    #print(reader.numPages)       #get number of pages
    page_file=reader.getPage(0)          #now page_file will savve first index page
    page_file.rotateCounterClockwise(90) #now page_file will roate saved page
    writer=PyPDF2.PdfFileWriter() #we are going to write something
    writer.addPage(page_file)       #yes we are writing on Page_file
    with open('tilt.pdf','wb') as new_file: #with within the with for saving
        writer.write(new_file) # roated page_file is created as tilt.pdf
'''
'''
input=sys.argv[1:]  #gets the arguments from the terminal before execution
def pdf_merger(pdf_list):
    merger=PyPDF2.PdfFileMerger() 
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")       #creating a new merged pdf without with open

pdf_merger(input)
'''
template = PyPDF2.PdfFileReader(open(r'C:\Users\nandu\Desktop\Python\pdfPlayground\super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open(r'C:\Users\nandu\Desktop\Python\pdfPlayground\wtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page_file=template.getPage(i)
    page_file.mergePage(watermark.getPage(0))
    output.addPage(page_file)
with open('watermarkouput.pdf','wb') as file:
    output.write(file)