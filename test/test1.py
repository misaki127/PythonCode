#encoding:utf-8
import requests
import pandas as pd
import xlwt

import numpy

def get_request(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        print('error!')


rus = get_request(url='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist')

rulse_list = rus['data']
name_list = []#国家名称
continent_list = []#所属大洲
time_list = []#日期
add_list = []#新增病例
toal_list = []#总计病例
dead_list = []#死亡病例
heal_list = []#治愈病例
now_list = []#现存病例
comp_list = []#总计疑似
now_comp_list = []#现存疑似
heal_comp_list = []#新增治愈
dead_comp_list=[]#新增死亡

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
for i in range(len(rulse_list)):
    name_list.append(rulse_list[i]['name'])
    continent_list.append(rulse_list[i]['continent'])
    time_list.append(rulse_list[i]['date'])
    add_list.append(rulse_list[i]['confirmAdd'])
    toal_list.append(rulse_list[i]['confirm'])
    dead_list.append(rulse_list[i]['dead'])
    heal_list.append(rulse_list[i]['heal'])
    now_list.append(rulse_list[i]['nowConfirm'])
    comp_list.append(rulse_list[i]['confirmCompare'])
    now_comp_list.append([rulse_list[i]['nowConfirmCompare']])
    heal_comp_list.append(rulse_list[i]['healCompare'])
    dead_comp_list.append(rulse_list[i]['deadCompare'])
df = pd.DataFrame({'国家名称':name_list,'所属大洲':continent_list,'日期':time_list,'新增病例':add_list,'总计病例':toal_list,'死亡病例':dead_list,'治愈病例':heal_list,'现存病例':now_list,'总计疑似':comp_list,
                   '现存疑似':now_comp_list,'新增治愈':heal_comp_list,'新增死亡':dead_comp_list})
print(type(df['国家名称']))

def write_excel(info_list,filename):
    wb = xlwt.Workbook('utf-8')
    ws = wb.add_sheet('新冠全球疫情情况')
    for i in range(len(info_list)):
        for b in range(len(info_list[i])):
            ws.write(i,b,info_list[i][b])
    wb.save(filename)



