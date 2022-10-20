from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.corpus import inaugural
from nltk.tokenize import word_tokenize
from pathlib import Path
import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

stop_words = set(stopwords.words('english'))
# filename = 'Test2.pdf'
# filenames = ['sample-pdf-download-10-mb.pdf', 'sample-pdf-file.pdf', 'sample-pdf-with-images.pdf']
filenames = ['Test2.pdf']
# keywords_list = [r'[Ll]orem', r'specimen book']
keywords_list = []
pdf_Writer = PdfFileWriter()

for filename in filenames:
    print(filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages

    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text_page = pageObj.extractText()
        text_line = text_page.split("\n")
        for i in range(0, 5):
            text += text_line[i]


    # text = 'I am a graduate. I want to learn Python. I like learning Python. Python is easy. Python is interesting. \
    # Learning increases thinking. Everyone should invest time in learning'
    total_words = text.split()
    total_word_length = len(total_words)
    print(total_word_length)
    print('------------------------------------------')
    total_sentences = tokenize.sent_tokenize(text)
    total_sent_len = len(total_sentences)
    print(total_sent_len)
    print('------------------------------------------')
    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())
    # print(tf_score)
    # print('------------------------------------------')


    def check_sent(word, sentences):
        final = [all([w in x for w in word]) for x in sentences]
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return int(len(sent_len))


    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    # Performing a log and divide
    idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())

    # print(idf_score)
    # print('------------------------------------------')

    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    # print(tf_idf_score)
    print('------------------------------------------')


    def get_top_n(dict_elem, n):
        result = dict(sorted(dict_elem.items(), key=itemgetter(0), reverse=True)[:n])
        print(dict(sorted(dict_elem.items(), reverse=True)[:n]))
        print('**********************************************************')
        return result


    key_list = get_top_n(tf_idf_score, 5)
    print(key_list)
    if list(key_list.keys()) != keywords_list:
        keywords_list.extend(key_list.keys())
    print(keywords_list)
    keywords_list = list(set(keywords_list))
    print(keywords_list)
    print('=========================================================================')


for filename in filenames:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages

    count = 0
    pre_count = 1
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text = pageObj.extractText()
        # print("here")
        # print(keywords_list)
        for keyword in keywords_list:
            keywords = re.findall(keyword, text)
            # keywords = re.search(keyword, text)
            # print(keywords)
            # print(len(keywords))
            if len(keywords) > 0:
                # if pre_count == 1 or count != pre_count:
                print(count) #, " ", keywords)
                # pre_count = count
