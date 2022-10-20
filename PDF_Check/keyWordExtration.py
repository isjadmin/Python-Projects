import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import json

filenames = ['Test2.pdf']
pdf_Writer = PdfFileWriter()


with open("config.json", "r") as config:
    keywords_list = json.load(config)
    print("Read successful")
# print(keywords_list)


for filename in filenames:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    writer_count = 0
    previous_count = 0
    bookmarkKeyList = {}

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
                text += text_line[i]
            '''if i >= (len_text_line-5):
                # print(text_line[i])
                text += text_line[i]'''
        new_keylist = []
        for key in keywords_list:
            keyword_list = keywords_list[key]
            # print(keyword_list)
            for keyword in keyword_list:
                keywords = re.findall(keyword, text)
                # print(len(keywords))
                if len(keywords) > 0:
                    # print('...........................................................................................')
                    # print(count, " ", keywords)
                    if keywords[0] == 'Questions (Page 1 of 5)':
                        keywords[0] = 'Questions \\(Page 1 of 5\\)'
                    if keywords[0] == 'Questions (Page 2 of 5)':
                        keywords[0] = 'Questions \\(Page 2 of 5\\)'
                    if keywords[0] == 'Questions (Page 3 of 5)':
                        keywords[0] = 'Questions \\(Page 3 of 5\\)'
                    if keywords[0] == 'Questions (Page 4 of 5)':
                        keywords[0] = 'Questions \\(Page 4 of 5\\)'
                    if keywords[0] == 'Questions (Page 5 of 5)':
                        keywords[0] = 'Questions \\(Page 5 of 5\\)'
                    new_keylist.append(keywords[0])
                    '''if count != 0 and count != previous_count:
                        pdf_Writer.addPage(pdfReader.getPage(count-1))  # insert page
                        pdf_Writer.addBookmark(key+'-'+keywords[0], writer_count, parent=None)  # add bookmark
                        pdf_Writer.setPageMode("/UseOutlines")  # This is what tells the PDF to open to bookmarks
                        with open("result.pdf", "wb") as fp:  # creating result pdf JCT
                            pdf_Writer.write(fp)  # writing to result pdf JCT

                        writer_count += 1'''
                    # previous_count = count
                    # print(previous_count)

            bookmarkKeyList[count] = new_keylist

    # print(bookmarkKeyList)
    page_bookmark = {}

    for page in bookmarkKeyList:
        # print(page)
        bookmark = []
        # print(len(bookmarkKeyList[page]))
        if len(bookmarkKeyList[page]) == 0:
            bookmark.append("Misc")
        else:
            for key in keywords_list:
                bkm_list = bookmarkKeyList[page]
                # print(bkm_list)
                pre_key = ""
                for bkm in bkm_list:
                    if bkm in keywords_list[key] and key != pre_key:
                        if page == 18:
                            print(bkm, " ", keywords_list[key])
                        bookmark.append(key)
                        pre_key = key

        page_bookmark[page] = bookmark

    # print(page_bookmark)

    final_filename = filename + "_result.pdf"
    flag = False

    for key in keywords_list:
        flag = True
        for page in page_bookmark:
            if key in page_bookmark[page]:
                pdf_Writer.addPage(pdfReader.getPage(page-1))  # insert page
                if flag:
                    pdf_Writer.addBookmark(key, writer_count, parent=None)  # add bookmark
                    flag = False
                pdf_Writer.setPageMode("/UseOutlines")  # This is what tells the PDF to open to bookmarks
                with open(final_filename, "wb") as fp:  # creating result pdf JCT
                    pdf_Writer.write(fp)  # writing to result pdf JCT

                writer_count += 1
    flag = True
    for page in page_bookmark:
        bk = page_bookmark[page]
        # print(bk)
        if len(bk) == 0 or bk[0] == 'Misc':
            pdf_Writer.addPage(pdfReader.getPage(page-1))  # insert page
            if flag:
                pdf_Writer.addBookmark('Misc', writer_count, parent=None)  # add bookmark
                flag = False
            pdf_Writer.setPageMode("/UseOutlines")  # This is what tells the PDF to open to bookmarks
            with open(final_filename, "wb") as fp:  # creating result pdf JCT
                pdf_Writer.write(fp)  # writing to result pdf JCT

            writer_count += 1


