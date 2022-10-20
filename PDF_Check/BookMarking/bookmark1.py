import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

filenames = ['Test2.pdf']
# filenames = ['sample-pdf-download-10-mb.pdf', 'sample-pdf-file.pdf', 'sample-pdf-with-images.pdf']
# keywords_list = [r'[Ll]orem', r'specimen book', r'F[f]orm']
keywords_list = [r'TAX ORGANIZER', r'Topic Index', r'Questions \(Page \w of 5\)', r'State Information',
                 r'Personal Information', r'Dependents and Wages', r'Direct Deposit and Withdrawal',
                 r'Electronic Filing', r'Engagement Letter', r'Friedman Letter', r'FLLP Letter',
                 r'HBK Letter', r'HBK Consent letter', r'Tax Engagement Letter', r'Driving License']
pdf_Writer = PdfFileWriter()

for filename in filenames:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    writer_count = 0
    # text = ""

    while count < num_pages:
        text = ""
        pageObj = pdfReader.getPage(count)
        count += 1
        text_page = pageObj.extractText()
        # text += text_page
        text_line = text_page.split("\n")
        len_text_line = len(text_line)
        for i in range(len_text_line):
            if i <= 6:
                # print(text_line[i])
                text += text_line[i]
            if i >= (len_text_line-5):
                # print(text_line[i])
                text += text_line[i]

        # if count == 122:
            # print(text)

        # for i in text_line:
        #     print(i)
        #     print('...............................................................................................')
        # print(count, "= ", pageObj.extractText().title())
        # print('...............................................................................................')

        for keyword in keywords_list:
            # print(keyword)
            if keyword == r'F[f]orm':
                # print("here")
                keywords = re.findall(r'[f,F]orm 1\w', text)
                # print(keywords)
            else:
                # print(keyword)
                keywords = re.findall(keyword, text)
            # print(len(keywords))
            if len(keywords) > 0:
                print('...........................................................................................')
                print(count, " ", keywords)
                pdf_Writer.addPage(pdfReader.getPage(count-1))  # insert page
                pdf_Writer.addBookmark(keywords[0], writer_count, parent=None)  # add bookmark
                pdf_Writer.setPageMode("/UseOutlines")  # This is what tells the PDF to open to bookmarks
                with open("Test2-Result.pdf", "wb") as fp:  # creating result pdf JCT
                    pdf_Writer.write(fp)  # writing to result pdf JCT

                writer_count += 1
