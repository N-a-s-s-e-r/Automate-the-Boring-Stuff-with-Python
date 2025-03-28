import ezsheets, re

#Access the spreadsheet
ss = ezsheets.Spreadsheet('1QYcQ1D2StPA5T5DIuAeT18-IKCi8GTY6EUjuLMthiVo')

emailList = []

for rowNum in range(2, ss[0].rowCount):     #Skips the first row
    if ss[0].getRow(rowNum)[2] != None:     #Eliminates empty cells
        emailRegex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        #Handles Nonetype Attribute error
        if (mo1 := emailRegex.search(ss[0].getRow(rowNum)[2])) is not None:
            emailList.append(mo1.group())

print(emailList)
