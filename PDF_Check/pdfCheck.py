'''# Reading Highlighted text
from PyPDF2 import PdfReader

reader = PdfReader("sample-pdf-download-10-mb.pdf")

for page in reader.pages:
    # print(page)
    if "/Annots" in page:
        print("here")
        # print(page["/Annots"])
        for annot in page["/Annots"]:
            print(annot)
            subtype = annot.get_object()["/Subtype"]
            print(subtype)
            if subtype == "/Highlight":
                coords = annot.get_object()["/QuadPoints"]
                x1, y1, x2, y2, x3, y3, x4, y4 = coords
                print(x1, y1, x2, y2, x3, y3, x4, y4)'''


'''# Reading Header and Footer
import tika
from tika import parser

FileName = "sample-pdf-download-10-mb.pdf"
PDF_Parse = parser.from_file(FileName)
print(PDF_Parse['content'])
print(PDF_Parse['metadata']) # Format-Dictionary'''


import PyPDF2
# Reading Page using page no.
file = open('Test2.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(file)
totalpages = readpdf.numPages

print(totalpages)

page = readpdf.pages[118]
print(page.extract_text())
