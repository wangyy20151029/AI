import xlrd

def getExcel(file_name='test.xlsx'):
    rows=[]
    book = xlrd.open_workbook(file_name)
    sheet=book.sheet_by_index(0)
    for row in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row,0,sheet.ncols)))
    return rows

if __name__ == '__main__':
    print(getExcel())