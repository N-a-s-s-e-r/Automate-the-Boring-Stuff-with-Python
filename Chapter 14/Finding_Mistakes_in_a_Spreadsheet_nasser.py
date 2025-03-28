import ezsheets

#Access the spreadsheet
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for rowNum in range(2, 15001):    # skip the first row
    if int(ss[0].getRow(rowNum)[0]) * int(ss[0].getRow(rowNum)[1]) == int(ss[0].getRow(rowNum)[2]):
        a = 1
    else:
        print(rowNum)
