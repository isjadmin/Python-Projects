import fitz
import json


'''def scrape(keyword, filePath):
    results = []  # list of tuples that store the information as (text, font size, font name)
    pdf = fitz.open(filePath)  # filePath is a string that contains the path to the pdf
    count = 0
    for page in pdf:
        print(page)
        print(type(page))
        count += 1
        dict = page.get_text("dict")
        # print(dict)
        blocks = dict["blocks"]
        # print(blocks)
        for block in blocks:
            if "lines" in block.keys():
                spans = block['lines']
                for span in spans:
                    data = span['spans']
                    for lines in data:
                        if lines['size'] > 10.5:
                            # print(lines['text'], lines['size'], lines['font'], count)
                            if keyword[0] in lines['text']:  # only store font information of a specific keyword
                                results.append((lines['text'], lines['size'], lines['font'], count))
                                # lines['text'] -> string, lines['size'] -> font size, lines['font'] -> font name
    pdf.close()
    return results'''


pdf = fitz.open('Test2.pdf')
total_pages = pdf.page_count

with open("config.json", "r") as config:
    keywords_list = json.load(config)
    print("Read successful")
# print(keywords_list)

for key in keywords_list:
    keyword_list = keywords_list[key]
    # print(keyword_list)
    key_store = {}
    for keyword in keyword_list:
        c = 0
        # print(scrape(keyword, 'Test2.pdf'))
        for page in range(0, total_pages):
            text = pdf[page]
            key_search = text.search_for(keyword)
            for keys in key_search:
                c += 1
        if c >= 1:
            key_store[keyword] = c
    if len(key_store) > 0:
        print(key_store)





########################################################################################################################
'''from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LTLine,LAParams
import os
path=r'/path/to/pdf'

Extract_Data=[]

for page_layout in extract_pages(path):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                for character in text_line:
                    if isinstance(character, LTChar):
                        Font_size=character.size
            Extract_Data.append([Font_size,(element.get_text())])'''


########################################################################################################################
'''import re
from PyPDF2 import PdfFileReader, PdfFileWriter

filenames = ['Test2.pdf']
keywords_list = {"Tax Organizer": [r'TAX ORGANIZER', r'Topic Index', r'Questions \(Page \w of 5\)', r'State Information',
                                   r'Personal Information', r'Dependents and Wages', r'Direct Deposit and Withdrawal',
                                   r'Electronic Filing', r'Engagement Letter', r'Friedman Letter', r'FLLP Letter',
                                   r'HBK Letter', r'HBK Consent letter', r'Tax Engagement Letter', r'Driving License'],
                 "Tax Information": [r'Email Information', r'Mail Info', r'Client Email', r'Mail Information',
                                     r'Tax Information', r'Check Information', r'Foreign Assets', r'FA', r'Foreign Tax',
                                     r'Foreign Taxes', r'FT', r'Foreign Incomes and Taxes Sumary', r'Notices from IRS',
                                     r'IRS Notice', r'IRS', r'Hand Written Info', r'Hand written tax information',
                                     r'Handwritten Info', r'Handwritten', 'Additional Information'],
                 "Wage Income": [r'W-2', r'Form W2', r'Earnings Statement'],
                 "Interest Income": [r'Interest Received', r'Interest Income', r'Form 1099-INT'],
                 "Dividend Income": [r'Dividend Received', r'Dividend Income', r'Form 1099-DIV'],
                 "Capital Gains and Losses": [r'Sales of Stocks', r'Securities', r'Capital Assets & Installment Sales',
                                              r'Settlement Statement', r'Closing Statement', r'HUD Statement',
                                              r'Installment Sales', r'Form 1099-B'],
                 "1099 Brokerages": [r'Brokerage', r'Broker', r'Name of Stock'],
                 "Business Income": [r'Business Income', r'P&L Statement', r'Business Expenses',
                                     r'Business Depreciation', r'Business Vehicle Expenses', r'Hand Written Business'],
                 "Rental Income": [r'Rental and Royalty Income', r'Rental Income', r'Rental and Royalty Expenses',
                                   r'Rental Expenses', r'Rental Property', r'Rental Depreciation',
                                   r'Rental Fixed Assets', r'Rental and Royalty Property and Equipment & Depletion',
                                   r'Rental Vehicle Expenses', r'Hand Written Rental'],
                 "Partnerships, S-Corporations, Trust": [r'Schedule K1 Information', r'Partnerships', r'S-Corporations',
                                                         r'Trust', r'K1 Letter Information', r'Form 1065 Sch K1',
                                                         r'Form 1120S Sch K1', r'Form 1041 Sch K1', r'Grantor Letter'],
                 "IRA & Pension": [r'IRA Information', r'Pension, Annuity and Retirement Plan Information',
                                   r'Form 1099-R', r'Pension Information', r'IRA Portfolio statement', r'Form 1099 R'],
                 "Miscellaneous Income": [r'Miscellaneous Income, Adjustments and Alimony', r'Miscellaneous Income',
                                          r'Adjustments and Alimony', r'Form 1099 SSA', r'Form 1099-NEC', r'W2G',
                                          r'Form 1099-Q', r'Form 1099-Misc', r'Form  1099-G', r'1099-SA'],
                 "Adjustments to Income": [r'Misc Adjustments', r'Miscellaneous Adjustments', r'Misc. Adj.',
                                           r'Tuition Fees', r'Misc. Adjustments', r'Form 1098-T', r'Form 1098T',
                                           r'Form 1098-E', r'Form 1098E', r'Form 5498-SA', r'Form 5498-IRA',
                                           r'Form 1098', r'Form 1098 MIS'],
                 "Itemized Deduction": [r'Medical and Taxes', r'Vision', r'Pharmacy Bills', r'Property Tax',
                                        r'RE Taxes',
                                        r'RE Taxes - Check', r'Personal Property Tax', r'Mortgage Interest',
                                        r'Mortgage Interest Statement', r'Contributions', r'Gifts Made in Trust',
                                        r'Gifts Made Outright to an Individual', r'Miscellaneous Deductions',
                                        r'Tax Preparation Fees', r'Accountant Fees', r'Tax Preparer Fees',
                                        r'Tax Prep Fees'],
                 "Credits & Other Taxes": [r'Credits & Other Taxes', r'Dependent care', r'Child and dependent care',
                                           r'Sch H', r'Household Employment Taxes', r'1095-A', r'1095-B', r'1095-C',
                                           r'Stimulus Recovery Rebate'],
                 "Estimated Tax Payments": [r'Federal Estimated Tax Payment', r'Form 1040-ES', r'Form 1040-V',
                                            r'Form 4868', r'State and City Estimated Tax Payment',
                                            r'State Tax Payments',
                                            r'State Estimated Tax Payments', r'Estimated Tax payment']
                 }
pdf_Writer = PdfFileWriter()

for filename in filenames:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
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
        for key in keywords_list:
            keyword_list = keywords_list[key]
            # print(keyword_list)
            for keyword in keyword_list:
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
                    pdf_Writer.addBookmark(key+'-'+keywords[0], writer_count, parent=None)  # add bookmark
                    pdf_Writer.setPageMode("/UseOutlines")  # This is what tells the PDF to open to bookmarks
                    with open("Bookmark-result.pdf", "wb") as fp:  # creating result pdf JCT
                        pdf_Writer.write(fp)  # writing to result pdf JCT

                    writer_count += 1'''


########################################################################################################################
'''import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

filenames = ['Test2.pdf']
# filenames = ['sample-pdf-download-10-mb.pdf', 'sample-pdf-file.pdf', 'sample-pdf-with-images.pdf']
# keywords_list = [r'[Ll]orem', r'specimen book', r'F[f]orm']
keywords_list = [r'TAX ORGANIZER', r'Topic Index', r'Questions \\(Page \\w of 5\\)', r'State Information',
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

                writer_count += 1'''

########################################################################################################################

'''from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

filename = r'Test2.pdf'
input_pdf = PdfFileReader(filename)

pdf_Writer = PdfFileWriter()

x = ['1-5', '50', '15-18']

for items in x:
    if '-' in items:
        x1 = items.split('-')
        x2 = list(map(int, x1))

        for i in range(x2[0] - 1, x2[1]):
            page = input_pdf.getPage(i)
            pdf_Writer.addPage(page)


    else:
        page = input_pdf.getPage(int(items) - 1)
        print(page)

        pdf_Writer.addPage(page)


    pdf_Writer.getNumPages()

    with Path(r'output.pdf').open(mode="wb") as output_file:
        pdf_Writer.write(output_file)'''
