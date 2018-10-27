import xlrd

workbook = xlrd.open_workbook('demo.xlsx')
worksheet = workbook.sheet_by_index(0)

data1 =[]

data1 = worksheet.col_values(0,0)
data2 = worksheet.col_values(1,0)

print(str(', '.join(data1)))
print(str(', '.join(data2)))