def row_to_list(df):
    rows = []
    sheet = df.sheet_by_index(0)

    for i in range(len(sheet.col(0))):
        rowList = []
        for j in range(len(sheet.row(0))):
            rowList.append(sheet.cell(i,j).value)
        rows.append(rowList)

    return rows

def column_to_list(df):
    columns = []
    sheet = df.sheet_by_index(0)

    for i in range(len(sheet.row(0))):
        columnList = []
        for j in range(len(sheet.col(0))):
            columnList.append(sheet.cell(j,i).value)
        columns.append(columnList)

    return columns