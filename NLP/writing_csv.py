# importing the csv module
import csv
from datetime import datetime

# field names
fields = ['name', 'mob no', 'email', 'created time', 'testscore', 'linked resume', 'notice period',
          'current ctc', 'expected ctc', 'skill1', 'skill1 years', 'skill2', 'skill2 years',
          'skill3', 'skill3 years']

# data rows of csv file
rows = [['abc', 1234567890, 'abc@gmail.com', datetime.strftime(datetime(2022, 11, 8, 9, 30),
                                                               '%Y, %m, %d, %H, %M, %S'),
         55, 'www.abc.com', 2, 5, 7.5, 'C', 1, 'Python', 2, None, None],
        ['efg', 2345678901, 'efg@yahoo.com', datetime.strftime(datetime(2022, 11, 9, 9, 30),
                                                               '%Y, %m, %d, %H, %M, %S'),
         66, 'www.efg.com', 3, 6.5, 9, 'C++', 2, 'JS', 1, 'React', 1],
        ['hij', 3456789912, None, datetime.strftime(datetime(2022, 11, 10, 9, 30),
                                                    '%Y, %m, %d, %H, %M, %S'),

         77, None, 2, 8, None, 'C', 3, 'Python', 2, 'Java', 5],
        [None, 4567900923, 'xyzoutlook.com', datetime.strftime(datetime(2022, 11, 11, 9, 30),
                                                               '%Y, %m, %d, %H, %M, %S'),
         88, 'www.abc.com', 3, 9.5, 12, 'C++', 2, 'JS', 5, 'React', 4],
        ['klm', 5679011934, 'klm@cvb.us', None, 99, 'www.efg.com', 2, 11, 13.5, 'C', 6, 'Python', 4, 'Java', 2],
        [None, 6790122945, 'asd@abc.in', datetime.strftime(datetime(2022, 11, 11, 9, 30),
                                                           '%Y, %m, %d, %H, %M, %S'),
         110, 'www.hij.com', None, None, 15, 'C++', 5, 'JS', 3, 'React', 8],
        ['nop', None, None, datetime.strftime(datetime(2022, 11, 14, 9, 30),
                                              '%Y, %m, %d, %H, %M, %S'),
         121, 'www.abc.com', 3, 14, 16.5, None, None, 'Python', 6, 'Java', 7],
        ['qrs', 901234490, 'qrs12@klm.au', '15-13-2000', 132, None, 2, 15.5, 18, 'C++', 3, 'JS', 8, None, None],
        [None, None, 'cb11@klmau', datetime.strftime(datetime(2022, 11, 16, 9, 30),
                                                     '%Y, %m, %d, %H, %M, %S'),
         143, 'www.hij.com', 1, 17, 19.5, 'C', 8, 'Python', 9, 'Java', 7],
        ['stu', 7901233956, 'stu12@klm.au', datetime.strftime(datetime(2022, 11, 17, 9, 30),
                                                              '%Y, %m, %d, %H, %M, %S'),
         154, 'www.abc.com', 2, 18.5, 21, 'C++', 4, None, None, 'React', 5],
        ['vwx', 1357986420, 'vwx13@klm.au', datetime.strftime(datetime(2022, 11, 18, 9, 30),
                                                              '%Y, %m, %d, %H, %M, %S'),
         165, 'www.efg.com', None, 20, 22.5, 'C', 6, 'Python', 7, 'Java', 4]]

# name of csv file
filename = "D:\\Python-Projects\\NLP\\File-validation\\Book2.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
