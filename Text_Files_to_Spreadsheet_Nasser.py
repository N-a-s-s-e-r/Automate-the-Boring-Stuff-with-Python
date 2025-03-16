import openpyxl
import pyinputplus as pyip

wb = openpyxl.Workbook() # Create a blank workbook.
sheet = wb.active # Get the active sheet.

files_number = pyip.inputInt(prompt='How many text files would you like to work with?: ')

for l in range(files_number):
    file_location = pyip.inputStr(prompt=r'What is the text file directory? eg. C:\\Users\\medis\\dfe.txt: ')

    with open(file_location, 'r') as fr:                # Loop that reads the text file lines
        lines = fr.readlines()                          #   Read the lines of data into a list
        lines = [line.rstrip('\n') for line in lines]   #   Clean up the lines of data
        for i in range(len(lines)):                     # Loop that writes to a spreadsheet
            sheet.cell(row=i+1, column=l+1).value = lines[i]

wb.save('Ditto.xlsx')
print('I\'m done, Check your working directory to see the magic of this program')
