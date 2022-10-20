import re
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

                    writer_count += 1
