# importing csv module
import csv
from datetime import datetime
import os
import re

# csv file name
filename = "D:\\Python-Projects\\NLP\\File-validation\\Book1.csv"

# initializing the titles and rows list
# fields = []
rows = []


fields_writing = ['name', 'mob no', 'email', 'created time', 'testscore', 'linked resume', 'notice period',
                  'current ctc', 'expected ctc', 'skill1', 'skill1 years', 'skill2', 'skill2 years',
                  'skill3', 'skill3 years', 'remark']

csv_success_row_list = []
csv_error_row_list = []
# csv_success_flag = True

remark = ""


def check_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, s):
        return True
    else:
        return False


# writing to csv file+
def file_writing(file_name, field_name, row_list):
    with open(file_name, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(field_name)

        # writing the data rows
        csvwriter.writerows(row_list)


# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

for row in rows:
    # parsing each column of a row
    count = 0
    csv_success_flag = True
    remark = ""
    if len(row) == 0:
        continue
    for col in row:
        # print(fields[count])
        '''print("%8s" % type(col), end="  ")
        print("%8s" % col, end="  ")'''
        if fields[count] == 'name':
            if len(col) > 0:
                print(col)
            else:
                print("incorrect name")
                csv_success_flag = False
                remark += "Invalid Name, "
        if fields[count] == 'mob no':
            try:
                print(int(col))
            except:
                print("incorrect mob no")
                csv_success_flag = False
                remark += "Invalid Mobile No., "
        if fields[count] == 'email':
            if check_email(col):
                print(col)
            else:
                csv_success_flag = False
                print("incorrect email")
                remark += "Invalid Email-ID, "
        if fields[count] == 'created time':
            try:
                time = col.split(',')
                for i in range(len(time)):
                    time[i] = int(time[i])
                print(time)
                print(datetime.strftime(datetime(time[0], time[1], time[2], time[3], time[4], time[5]),
                                        '%Y, %m, %d, %H, %M, %S'))
            except:
                csv_success_flag = False
                print("Incorrect Created Date")
                remark += "Invalid Created Date, "
        if fields[count] == 'testscore':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect test score")
                remark += "Invalid Test Score, "
        if fields[count] == 'linked resume':
            if len(col) > 0:
                print(col)
            else:
                print("incorrect linked resume")
        if fields[count] == 'notice period':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect notice period")
                remark += "Invalid Notice Period, "
        if fields[count] == 'current ctc':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect current ctc")
                remark += "Invalid Current CTC, "
        if fields[count] == 'expected ctc':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect expected ctc")
                remark += "Invalid Excepted CTC, "
        if fields[count] == 'skill1':
            if len(col) > 0:
                print(col)
            else:
                print("incorrect skill1")
                remark += "Invalid Skill1, "
        if fields[count] == 'skill1 years':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect skill1 years")
                remark += "Invalid Skill1 Years, "
        if fields[count] == 'skill2':
            if len(col) > 0:
                print(col)
            else:
                print("incorrect skill2")
                remark += "Invalid Skill2, "
        if fields[count] == 'skill2 years':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect skill2 years")
                remark += "Invalid Skill2 Years, "
        if fields[count] == 'skill3':
            if len(col) > 0:
                print(col)
            else:
                print("incorrect skill3")
                remark += "Invalid Skill3, "
        if fields[count] == 'skill3 years':
            try:
                if '.' in col:
                    print(float(col))
                else:
                    print(int(col))
            except:
                print("incorrect skill3 years")
                remark += "Invalid Skill3 Years, "
        if count < len(fields)-1:
            count += 1
    row.append(remark.removesuffix(', '))
    if csv_success_flag:
        csv_success_row_list.append(row)
    else:
        csv_error_row_list.append(row)


print(csv_error_row_list)
print(csv_success_row_list)

# name of csv file
success_filename = filename.removesuffix('.csv') + '-Success.csv'
file_writing(success_filename, fields_writing, csv_success_row_list)

error_filename = filename.removesuffix('.csv') + '-Error.csv'
file_writing(error_filename, fields_writing, csv_error_row_list)
