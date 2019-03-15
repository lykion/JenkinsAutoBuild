# -*- coding:utf-8 -*-
import os
import xlrd

string = 'Hello World,I am your best friend'
print(string)

path = os.path.join(os.getcwd(), 'API_Case.xlsx')
print(path)

workbook = xlrd.open_workbook(path)
worksheet = workbook.sheets()[0]
print(worksheet.name)

rows = worksheet.nrows
print(rows)
print("================= 开始读取Excel文件 =================")
for i in range(1, rows):
    id = int(worksheet.cell_value(i, 0))
    name = worksheet.cell_value(i, 1)
    host = worksheet.cell_value(i, 2)
    url = worksheet.cell_value(i, 3)
    method = worksheet.cell_value(i, 4)
    data = worksheet.cell_value(i, 7)
    print(id, name, host, url, method, data)
print("================= Excel文件读取结束 =================")
