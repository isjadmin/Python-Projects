# importing the csv module
import csv
from datetime import datetime

# field names
fields = ['name', 'mob no', 'email', 'created time', 'testscore', 'linked resume', 'notice period',
          'current ctc', 'expected ctc', 'skill1', 'skill1 years', 'skill2', 'skill2 years',
          'skill3', 'skill3 years']

date_time = datetime.strptime('08-Jan-2022 9:30:00', '%d-%b-%Y %H:%M:%S')
print(date_time)
d_type = type(date_time)
print(d_type)
if str(d_type) == "<class 'datetime.datetime'>":
    print(True)
else:
    print(False)


print(str(type(2)))
if str(type(2)) == "<class 'int'>":
    print(True)
else:
    print(False)


print(str(type(2.0)))
if str(type(2.0)) == "<class 'float'>":
    print(True)
else:
    print(False)


dig = '22.1'
print(dig)
print(dig.isdigit())


test_list = {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}
for num in test_list:
    print(test_list[num])
    print(num)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 5, 2):
    print("i:", i)
    print("i+2:", i+2)
    print(num[i+2])

# data rows of csv file
rows = [['abc', 1234567890, 'abc@gmail.com', '08-Jan-2022 9:30:00',
         55, 'www.abc.com', 2, 5, 7.5, 'C', 1, 'Python', 2, None, None],
        ['efg', 2345678901, 'efg@yahoo.com', '09-Jan-2022 9:30:00',
         66, 'www.efg.com', 3, 6.5, 9, 'C++', 2, 'JS', 1, 'React', 1],
        ['hij', 3456789912, None, '10-Jan-2022 9:30:00', 77, None, 2, 8, None, 'C', 3, 'Python', 2, 'Java', 5],
        [None, 4567900923, 'xyzoutlook.com', '11-Jan-2022 9:30:00', 88, 'www.abc.com', 3, 9.5, 12,
         'C++', 2, 'JS', 5, 'React', 4],
        ['klm', 5679011934, 'klm@cvb.us', None, 99, 'www.efg.com', 2, 11, 13.5, 'C', 6, 'Python', 4, 'Java', 2],
        [None, 6790122945, 'asd@abc.in', '12-Jan-2022 9:30:00',
         110, 'www.hij.com', None, None, 15, 'C++', 5, 'JS', 3, 'React', 8],
        ['nop', None, None, '13-Jan-2022 9:30:00',
         121, 'www.abc.com', 3, 14, 16.5, None, None, 'Python', 6, 'Java', 7],
        ['qrs', 901234490, 'qrs12@klm.au', '15-13-2000', 132, None, 2, 15.5, 18, 'C++', 3, 'JS', 8, None, None],
        [None, None, 'cb11@klmau', '14-Jan-2022 9:30:00',
         143, 'www.hij.com', 1, 17, 19.5, 'C', 8, 'Python', 9, 'Java', 7],
        ['stu', 7901233956, 'stu12@klm.au', '15-Jan-2022 9:30:00',
         154, 'www.abc.com', 2, 18.5, 21, 'C++', 4, None, None, 'React', 5],
        ['vwx', 1357986420, 'vwx123@klm.au', '16-Jan-2022 9:30:00', 165,
         'https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true',
         None, 20, 22.5, 'C', 6, 'Python', 7, 'Java', 4]]

'''# name of csv file
filename = "D:\\Python-Projects\\NLP\\File-validation\\Book1.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)'''
