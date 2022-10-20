import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import json
import fitz

filenames = ['Test2.pdf']
pdf_Writer = PdfFileWriter()


with open("config.json", "r") as config:
    keywords_list = json.load(config)
    print("Read successful")
# print(keywords_list)


def scrape(key_list, filePath, page_no):
    results = {}  # list of tuples that store the information as (text, font size, font name)
    pdf = fitz.open(filePath)  # filePath is a string that contains the path to the pdf
    count = 0
    for page in pdf:
        # print(page)
        count += 1
        if count == page_no:
            # print(type(page))
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
                            # print(lines)
                            if lines['size'] > 12.0:
                                # print(lines['text'], lines['size'], lines['font'], count)
                                for keyword in key_list:
                                    if keyword in lines['text']:  # only store font information of a specific keyword
                                        results[lines['text']] = lines['size']
            break
    pdf.close()
    return results


for filename in filenames:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    writer_count = 0
    previous_count = 0
    bookmarkKeyList = {}
    result = {}

    while count < num_pages:
        text = ""
        pageObj = pdfReader.getPage(count)
        count += 1
        text_page = pageObj.extractText()

        # text += text_page
        text_line = text_page.split("\n")
        len_text_line = len(text_line)
        for i in range(0, len_text_line):
            if i <= 10:
                # print(text_line[i])
                # text += text_line[i]
                for key in keywords_list:
                    keyword_list = keywords_list[key]
                    # print(keyword_list)
                    for keyword in keyword_list:
                        if keyword in text_line[i]:
                            keywords = keyword.split()
                            keywords.append(keyword)
                            # print(keywords)
                            result["page_no"] = count
                            result["keyword"] = keywords
                            result["property"] = scrape(keywords, filename, count)
                            print(keyword, "--->", count, "--->", i)
                            print(result)
