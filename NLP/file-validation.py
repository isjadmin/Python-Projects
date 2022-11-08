import openpyxl
from openpyxl import Workbook
import re
import datetime
import time

# Give the location of the file
path = ".\File-validation\Book1.xlsx"

# To open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path)

# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active

# Getting the value of maximum rows
# and column
row = sheet_obj.max_row
column = sheet_obj.max_column

print("Total Rows:", row)
print("Total Columns:", column)


'''for i in range(1, column + 1):
    print(sheet_obj.cell(row=1, column=i).value)'''

success_row_list = [['name', 'mob no', 'email', 'created time', 'testscore', 'linked resume', 'notice period',
                     'current ctc', 'expected ctc', 'skill1', 'skill1 years', 'skill2', 'skill2 years',
                     'skill3', 'skill3 years', 'remark']]
error_row_list = [['name', 'mob no', 'email', 'created time', 'testscore', 'linked resume', 'notice period',
                   'current ctc', 'expected ctc', 'skill1', 'skill1 years', 'skill2', 'skill2 years',
                   'skill3', 'skill3 years', 'remark']]
success_flag = True
remark = ""


def check_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, s):
        return True
    else:
        return False


for j in range(2, row + 1):
    success_flag = True
    # time.sleep(2)
    row_list = []
    remark = ""
    for i in range(1, column + 1):
        # print(sheet_obj.cell(row=j, column=i).value)
        if sheet_obj.cell(row=1, column=i).value == 'name':
            # print('name: ', type(sheet_obj.cell(row=j, column=i).value))
            name = sheet_obj.cell(row=j, column=i).value
            row_list.append(name)
            if name is None or type(name) != str:
                success_flag = False
                remark += "Invalid name, "
        if sheet_obj.cell(row=1, column=i).value == 'mob no':
            # print('mob no: ', type(sheet_obj.cell(row=j, column=i).value))
            mob_no = sheet_obj.cell(row=j, column=i).value
            row_list.append(mob_no)
            if mob_no is None or type(mob_no) != int or len(str(mob_no)) < 10:
                success_flag = False
                remark += "Invalid Mob No., "
        if sheet_obj.cell(row=1, column=i).value == 'email':
            # print('email: ', type(sheet_obj.cell(row=j, column=i).value))
            email_id = sheet_obj.cell(row=j, column=i).value
            row_list.append(email_id)
            if email_id is None or check_email(email_id) is False:
                success_flag = False
                remark += "Invalid Email-ID, "
        if sheet_obj.cell(row=1, column=i).value == 'created time':
            # print('created time: ', type(sheet_obj.cell(row=j, column=i).value))
            created_time = sheet_obj.cell(row=j, column=i).value
            row_list.append(created_time)
            if created_time is None or type(created_time) != datetime.datetime:
                success_flag = False
                remark += "Invalid Created Time, "
        if sheet_obj.cell(row=1, column=i).value == 'testscore':
            # print('testscore: ', type(sheet_obj.cell(row=j, column=i).value))
            test_score = sheet_obj.cell(row=j, column=i).value
            row_list.append(test_score)
            if test_score is None or (type(test_score) != float and type(test_score) != int):
                remark += "Invalid Test Score, "
        if sheet_obj.cell(row=1, column=i).value == 'linked resume':
            # print('linked resume: ', type(sheet_obj.cell(row=j, column=i).value))
            linked_resume = sheet_obj.cell(row=j, column=i).value
            row_list.append(linked_resume)
            if linked_resume is None or type(linked_resume) != str:
                remark += "Invalid Linked Resume, "
        if sheet_obj.cell(row=1, column=i).value == 'notice period':
            # print('notice period: ', type(sheet_obj.cell(row=j, column=i).value))
            notice_period = sheet_obj.cell(row=j, column=i).value
            row_list.append(notice_period)
            if notice_period is None or (type(notice_period) != float and type(notice_period) != int):
                remark += "Invalid Notice Period, "
        if sheet_obj.cell(row=1, column=i).value == 'current ctc':
            # print('current ctc: ', type(sheet_obj.cell(row=j, column=i).value))
            current_ctc = sheet_obj.cell(row=j, column=i).value
            row_list.append(current_ctc)
            if current_ctc is None or (type(current_ctc) != float and type(current_ctc) != int):
                remark += "Invalid Current CTC, "
        if sheet_obj.cell(row=1, column=i).value == 'expected ctc':
            # print('expected ctc: ', type(sheet_obj.cell(row=j, column=i).value))
            expected_ctc = sheet_obj.cell(row=j, column=i).value
            row_list.append(expected_ctc)
            if expected_ctc is None or (type(expected_ctc) != float and type(expected_ctc) != int):
                remark += "Invalid Expected CTC, "
        if sheet_obj.cell(row=1, column=i).value == 'skill1':
            # print('skill1: ', type(sheet_obj.cell(row=j, column=i).value))
            skill1 = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill1)
            if skill1 is None or type(skill1) != str:
                remark += "Invalid Skill1, "
        if sheet_obj.cell(row=1, column=i).value == 'skill1 years':
            # print('skill1 years: ', type(sheet_obj.cell(row=j, column=i).value))
            skill1_years = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill1_years)
            if skill1_years is None or (type(skill1_years) != float and type(skill1_years) != int):
                remark += "Invalid Skill1 Years, "
        if sheet_obj.cell(row=1, column=i).value == 'skill2':
            # print('skill2: ', type(sheet_obj.cell(row=j, column=i).value))
            skill2 = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill2)
            if skill2 is None or type(skill2) != str:
                remark += "Invalid Skill2, "
        if sheet_obj.cell(row=1, column=i).value == 'skill2 years':
            # print('skill2 years: ', type(sheet_obj.cell(row=j, column=i).value))
            skill2_years = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill2_years)
            if skill2_years is None or (type(skill2_years) != float and type(skill2_years) != int):
                remark += "Invalid Skill2 Years, "
        if sheet_obj.cell(row=1, column=i).value == 'skill 3':
            # print('skill 3: ', type(sheet_obj.cell(row=j, column=i).value))
            skill3 = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill3)
            if skill3 is None or type(skill3) != str:
                remark += "Invalid Skill3, "
        if sheet_obj.cell(row=1, column=i).value == 'skill3 years':
            # print('skill3 years: ', type(sheet_obj.cell(row=j, column=i).value))
            skill3_years = sheet_obj.cell(row=j, column=i).value
            row_list.append(skill3_years)
            if skill3_years is None or (type(skill3_years) != float and type(skill3_years) != int):
                remark += "Invalid Skill3 Years, "
    row_list.append(remark.removesuffix(', '))
    print(row_list)
    print('-------------------------------------------------------------------------------------------------------')
    if success_flag:
        print(success_flag)
        print(row_list)
        success_row_list.append(row_list)
    else:
        print(success_flag)
        print(row_list)
        error_row_list.append(row_list)


print(success_row_list)
print(error_row_list)

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
workbook = Workbook()

# Anytime you modify the Workbook object
# or its sheets and cells, the spreadsheet
# file will not be saved until you call
# the save() workbook method.
success_file_name = path.removesuffix('.xlsx') + '-Success.xlsx'
error_file_name = path.removesuffix('.xlsx') + '-Error.xlsx'
workbook.save(filename=success_file_name)

wb_success = openpyxl.load_workbook(success_file_name)

sheet_success = wb_success.active

for rows in tuple(success_row_list):
    sheet_success.append(tuple(rows))

workbook = Workbook()
workbook.save(filename=error_file_name)
wb_success.save(success_file_name)

wb_error = openpyxl.load_workbook(error_file_name)

sheet_error = wb_error.active

for rows in tuple(error_row_list):
    sheet_error.append(tuple(rows))

wb_error.save(error_file_name)

