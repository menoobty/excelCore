from reader.read import read_excel
from driver import excel_parser
from calculator.calculate import calculate
from writer.write import append_to_excel

def process():
    dateFrame = read_excel()
    columns = excel_parser.column_to_list(dateFrame)
    result = calculate(columns)
    append_to_excel(dateFrame,result)
    print (result)

process()