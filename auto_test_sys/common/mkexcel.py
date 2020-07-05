#encoding：utf-8

import xlrd
import xlwt

def read_excel(filename):   #读取excel文件，返回一个数组（全部的表名，全部的数据）   全部的数据是一个三层列表对象，最小一层为一行的数据，第二层为一张表的数据，第三层为整个文件的数据
    all_data = {}
    wb = xlrd.open_workbook(filename)
    sheets = wb.sheet_names()
    for i in sheets:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows
        clos = sheet.ncols
        num_list = []
        for a in range(rows):
            row_list = []
            for b in range(clos):
                ctype = sheet.cell(a,b).ctype
                cell = sheet.cell_value(a,b)
                if ctype == 2 and cell % 1 == 0.0:
                    cell = int(cell)
                row_list.append(str(cell))
            num_list.append(row_list)
        all_data[i] = num_list
    return sheets,all_data

def write_excel(filename,sheetnames,info_list):#写入一个excel 数据格式为([sheetname]，{sheetname1:[data],sheetname2:[data]})
    workbook = xlwt.Workbook()
    for i in sheetnames:
        sheetname = i.encode('utf-8')
        worksheet = workbook.add_sheet(sheetname)
        for a in range(len(info_list[i])):
            for b in range(len(info_list[i][a])):
                worksheet.write(a,b, info_list[i][a][b])

    workbook.save(filename)


