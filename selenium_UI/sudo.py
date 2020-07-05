#encoding:utf-8
import time

sodo_list = [[0,0,0,6,0,0,0,5,0],
             [8,0,4,0,0,0,6,0,0],
             [0,2,0,0,8,0,0,3,0],
             [0,0,0,7,0,3,0,0,4],
             [0,0,6,0,5,0,1,0,0],
             [3,0,0,1,0,8,0,0,0],
             [0,7,0,0,1,0,0,2,0],
             [0,0,2,0,0,0,3,0,1],
             [0,9,0,0,0,7,0,0,0]]#初始数独
#sodo_list = [[9, 1, 7, 6, 3, 2, 4, 5, 8], [8, 3, 4, 9, 7, 5, 6, 1, 2], [6, 2, 5, 4, 8, 1, 7, 3, 9], [0, 5, 0, 7, 0, 3, 0, 0, 4], [0, 0, 6, 2, 5, 0, 1, 0, 0], [3, 0, 9, 1, 0, 8, 0, 0, 0], [0, 7, 0, 0, 1, 0, 0, 2, 0], [0, 0, 2, 0, 0, 0, 3, 0, 1], [0, 9, 0, 0, 0, 7, 0, 0, 0]]
address_list = [11,12,13,14,15,16,17,18,19]


starttime = time.time()


def jiancha(sodo_list):#查询
    chose_list = {}#每一个格子的位置信息和可填写信息
    for a in range(9):  #九宫格
        for b in range(9):
            if sodo_list[a][b]==0:
                num_list =set({1, 2, 3, 4, 5, 6, 7, 8, 9})
                set_list = []

                if a>=0 and a<=2:
                    if b>=0 and b <=2:
                        for p in range(3):
                            for q in range(3):
                                set_list.append(sodo_list[p][q])
                    elif b>=3 and b<=5:
                        for p in range(3):
                            for q in range(3,6):
                                set_list.append(sodo_list[p][q])
                    elif b>=6 and b<=8:
                        for p in range(3):
                            for q in range(6,9):
                                set_list.append(sodo_list[p][q])
                    else:
                        print('error')
                elif a>=3 and a<=5:
                    if b>=0 and b <=2:
                        for p in range(3,6):
                            for q in range(3):
                                set_list.append(sodo_list[p][q])
                    elif b>=3 and b<=5:
                        for p in range(3,6):
                            for q in range(3,6):
                                set_list.append(sodo_list[p][q])
                    elif b>=6 and b<=8:
                        for p in range(3,6):
                            for q in range(6,9):
                                set_list.append(sodo_list[p][q])
                    else:
                        print('error')
                elif a>=6 and a<=8:
                    if b>=0 and b <=2:
                        for p in range(6,9):
                            for q in range(3):
                                set_list.append(sodo_list[p][q])
                    elif b>=3 and b<=5:
                        for p in range(6,9):
                            for q in range(3,6):
                                set_list.append(sodo_list[p][q])
                    elif b>=6 and b<=8:
                        for p in range(6,9):
                            for q in range(6,9):
                                set_list.append(sodo_list[p][q])
                    else:
                        print('error')
                else:
                    print('error!')

                #行/列
                for l in range(9):
                    set_list.append(sodo_list[a][l])
                    set_list.append(sodo_list[l][b])
                #过滤
                set_list=set(set_list)
                set_list.remove(0)
                num_list = num_list-set_list
                l_list = []
                for i in range(len(num_list)):
                    l_list.append(num_list.pop())
                chose_list[str(a)+str(b)]=l_list
            else:
                pass
    return chose_list

def paixu(list):#排序
    sorted_x = sorted(list.items(),key = lambda i:len(i[1]))#通过列表长度排序，x.items把字典的一个元素返回为一个元素（key,values)
    return sorted_x

x = jiancha(sodo_list)
sorted_x = paixu(x)

#主程序
log_list = []#记录表
copy_list = sodo_list.copy()#备份数独列表
op = {}
for s in range(9):
    for d in range(9):
        l = str(s)+str(d)
        op[l]=[]
lenn = 0
while len(sorted_x)!=0:#进入循环
    try:
        while len(sorted_x[0][1]) == 0:
            #前面出错了
            for h in range(len(op[sorted_x[0][0]])):#去掉已经用过的数字
                sorted_x[0][1].remove(op[sorted_x[0][0]][h])
            while len(log_list[-1][1]) == 1:#检查回溯一步是否有多个选择，没有就再回溯一次，直到有多个选择
                copy_list[int(log_list[-1][0][0])][int(log_list[-1][0][1])]=0
                log_list.remove(log_list[-1])
            op[log_list[-1][0]].append(log_list[-1][1][0])#保存已使用过的数据
            if len(log_list)<lenn:  #释放已使用的数字
                op = {}
                for s in range(9):
                    for d in range(9):
                        l = str(s) + str(d)
                        op[l] = []
            lenn = len(log_list)#如果回溯到记录使用过数据之前，则释放保存的已使用的数据
            log_list[-1][1].remove(log_list[-1][1][0])#去掉刚刚用过的数据

            # print(c)

            if len(log_list[-1][1]) == 0:#如果本次回溯所有的数据都使用完毕，则继续往前回溯
                copy_list[int(log_list[-1][0][0])][int(log_list[-1][0][1])]=0
                log_list.remove(log_list[-1])

            copy_list[int(log_list[-1][0][0])][int(log_list[-1][0][1])] = int(log_list[-1][1][0])#选择数据填入
            chose_list = jiancha(copy_list)#查询
            sorted_x = paixu(chose_list)#排序
        copy_list[int(sorted_x[0][0][0])][int(sorted_x[0][0][1])] = int(sorted_x[0][1][0])#选择数据填入
        log_list.append(sorted_x[0])#记录操作
        chose_list = jiancha(copy_list)#查询
        sorted_x = paixu(chose_list)#排序
    except:
        pass
endtime = time.time()
for t in range(len(copy_list)):
    print(copy_list[t])
print('花费时间：')
print(endtime-starttime)

