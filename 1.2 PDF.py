import PyPDF4, os
os.chdir(r'C:\Users\zchen\OneDrive\Documents\Fungi internship\Research paper+ Slides')
pdf= open('Function of plant genes.pdf', 'rb') # read binary mode
reader= PyPDF4.PdfFileReader(pdf)
print(reader.numPages)
page= reader.getPage(0)
print(page.extractText()) # extracts text from page 2

pdf1= open(r'Conekt paper.pdf', 'rb')
reader1= PyPDF4.PdfFileReader(pdf1)

# Combine both files
writer= PyPDF4.PdfFileWriter()
for pagenum in range(reader.numPages):
    page= reader.getPage(pagenum)
    writer.addPage(page)

for pagenum in range(reader1.numPages):
    page= reader1.getPage(pagenum)
    writer.addPage(page)

os.chdir(r'C:\Users\zchen\OneDrive\Documents\Python stuff\Automate The Boring Stuff')
outputfile= open('combined pdf.pdf', 'wb') # write binary
writer.write(outputfile)
outputfile.close()
pdf1.close()
pdf.close()