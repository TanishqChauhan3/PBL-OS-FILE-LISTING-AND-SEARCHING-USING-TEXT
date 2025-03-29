# Import the libraries
import os
import pandas as pd

# Assign the variables
sourceLoc = "D:/Learnerea/others/"
outLoc = "D:/Learnerea/temp/"
searchString = "LEARNEREA"

direc = os.listdir(sourceLoc)
fileList = []

# For loop to search for the string in all files
for file in direc:
    try:
        # Try to open and read the file as text
        with open(sourceLoc + file, 'r', encoding='utf-8') as f:
            if searchString in f.read():
                fileList.append(file)
    except:
        # If there's an error (like binary files), skip the file
        continue

# DataFrame creation and export to excel
stringFile = pd.DataFrame(fileList, columns=['FileName'], index=range(0, len(fileList)))
stringFile.to_excel(outLoc + "stringFile.xlsx", index=False)                  
