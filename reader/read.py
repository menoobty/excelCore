from xlrd import open_workbook
import os

FILE_NAME =  'predictions.xlsx'
FILE_NAME_NEW = 'predictions.xls'

def getProjectFolder():
    currentFolder = os.getcwd()
    projectFolder = os.path.split(currentFolder)[0]
    return projectFolder


def generateFileName(fileName):
    projectFolder = getProjectFolder()
    excelFileName = os.path.join(projectFolder,fileName)
    return excelFileName


def read_excel():
    excelFileName = generateFileName(FILE_NAME)
    excelFileNameNew = generateFileName(FILE_NAME_NEW)
    df = None

    for fileName in (excelFileName,excelFileNameNew):
        try:
            df = open_workbook(excelFileName)
            break
        except:
            continue

    return df

a = getProjectFolder()
b = generateFileName(predictions.xlsx)
c = read_excel(b)
print(c.keys())


# df = pd.read_excel(io=file_name, sheet_name=sheet)
# print(len(df))
# keys = df.keys()
# print(keys)
# values = df['Yunus']
#
# print(type(values[0]))

#print(df.head(5))  # print first 5 rows of the dataframe