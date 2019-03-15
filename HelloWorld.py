# -*- coding:utf-8 -*-
import os
import xlrd
from log import LOG

string = 'Hello World,I am your best friend'
LOG().info(string)

path = os.path.join(os.getcwd(), 'API_Case.xlsx')
LOG().info(path)

workbook = xlrd.open_workbook(path)
worksheet = workbook.sheets()[0]
LOG().info(worksheet.name)

rows = worksheet.nrows
LOG().info(rows)
LOG().info("================= 开始读取Excel文件 =================")
for i in range(1, rows):
    id = int(worksheet.cell_value(i, 0))
    name = worksheet.cell_value(i, 1)
    host = worksheet.cell_value(i, 2)
    url = worksheet.cell_value(i, 3)
    method = worksheet.cell_value(i, 4)
    data = worksheet.cell_value(i, 7)
    LOG().info(id)
    LOG().info(name)
    LOG().info(host)
    LOG().info(url)
    LOG().info(method)
    LOG().info(data)
LOG().info("================= Excel文件读取结束 =================")
