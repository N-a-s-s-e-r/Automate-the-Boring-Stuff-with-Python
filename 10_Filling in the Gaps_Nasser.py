import shutil, os, re

# Create a regex that matches files with the File Name Pattern.
FileNamePattern = re.compile(r"^(.*?)((\d)*\d)")

#Sort the files
file_list = os.listdir(r'C:\Users\ekull\Downloads\spam')
file_list.sort()

FileNumber = []
i = 0

# Loop over the files in the working directory.
for OldFileName in file_list:
    mo = FileNamePattern.search(OldFileName)

    if mo == None:
        continue

    beforePart = mo.group(1)
    NumberingPart  = int(mo.group(2))

    i += NumberingPart
    FileNumber.append(NumberingPart)

    if len(FileNumber) == 1:
        continue
    elif len(FileNumber) > 1:
        FileNumber[-1] = FileNumber[-2] + 1

    # Form the new file name.
    NewFileFame = beforePart + str(FileNumber[-1])

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(r'C:\Users\ekull\Downloads\spam')
    OldFileName = os.path.join(absWorkingDir, OldFileName)
    NewFileFame = os.path.join(absWorkingDir, NewFileFame)

    #Rename the files.
    print(f'Renaming "{OldFileName}" to "{NewFileFame}"...')
    shutil.move(OldFileName, NewFileFame)

#print(FileNumber)
