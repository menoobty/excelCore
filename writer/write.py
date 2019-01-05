FILE_NAME =  'predictions_calculated.xls'

from xlutils.copy import copy
from reader.read import generateFileName
import os

def generateExcelPath():
    readFileName = generateFileName()
    folderPath = os.path.split(readFileName)[0]
    return os.path.join(folderPath,FILE_NAME)

def append_to_excel(df,points):
    excelContent = copy(df)
    originalSheet = df.sheet_by_index(0)
    sheetToWrite = excelContent.get_sheet(0)
    startRowIndex = len(originalSheet.col(0)) - 1
    rowLength = len(originalSheet.row(0))
    i = 1
    while i < rowLength:
        player = originalSheet.cell(0,i).value
        sheetToWrite.write(startRowIndex,i,points[player])
        i+=1
    excelContent.save(generateExcelPath())

