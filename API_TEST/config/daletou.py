import random
import time


def daletou(str_num):
    list0 = []
    success = 0
    while success < 7:
        str1 = str_num
        list3 = str1.split()
        print(list3)
        if len(list3) >= 7:
            for p in list3:
                list0.append(int(p))
            for i in range(5):
                if list0[i] >= 1 and list0[i] <= 35:
                    success += 1
                else:
                    pass
            for f in range(5,7):
                if list0[f] >= 1 and list0[f] <= 12:
                    success += 1
                else:
                    pass
            if success < 7:
                print("输入有误，请重新输入！")
            else:
                pass
        else:
            print("请重新输入！")

    list1 = [[],[]]
    a = 0
    while len(list1[0]) < 5:
        list1[0] = set(list1[0])
        a = random.randint(1,36)
        list1[0].add(a)
        list1[0] = set(list1[0])

    while len(list1[1]) < 2:
        list1[1] = set(list1[1])
        a = random.randint(1,13)
        list1[1].add(a)
        list1[1] = set(list1[1])

    list2 = [[list0[0],list0[1],list0[2],list0[3],list0[4]],[list0[5],list0[6]]]
    a = [x for x in list2[0] if x in list1[0]]
    b = [y for y in list2[1] if y in list1[1]]
    if a == 5 :
        if b == 0 :
            print("恭喜你获得三等奖")
            return 3
        elif b == 1:
            print("恭喜你获得二等奖")
            return 2
        elif b == 2:
            print("恭喜你获得一等奖")
            return 1
        else:
            print("服务错误！")
    elif a == 4 :
        if b == 0 :
            print("恭喜你获得七等奖")
            return 7
        elif b == 1:
            print("恭喜你获得五等奖")
            return 5
        elif b == 2:
            print("恭喜你获得四等奖")
            return 4
        else:
            print("服务错误！")
    elif a == 3 :
        if b == 0 :
            print("恭喜你获得九等奖")
            return 9
        elif b == 1:
            print("恭喜你获得八等奖")
            return 8
        elif b == 2:
            print("恭喜你获得六等奖")
            return 6
        else:
            print("服务错误！")
    elif a == 2 :
        if b == 0 :
            print("您没中奖！")
            return 0
        elif b == 1:
            print("恭喜你获得九等奖")
            return 9
        elif b == 2:
            print("恭喜你获得八等奖")
            return 8
        else:
            print("服务错误！")
    elif a == 1:
        if b == 0 :
            print("您没中奖！")
            return 0
        elif b == 1:
            print("您没中奖！")
            return 0
        elif b == 2:
            print("恭喜你获得九等奖")
            return 9
        else:
            print("服务错误！")
    elif a == 0 :
        if b == 0 :
            print("您没中奖！")
            return 0
        elif b == 1:
            print("您没中奖！")
            return 0
        elif b == 2:
            print("恭喜你获得九等奖")
            return 9
        else:
            print("服务错误！")
    else:
        print("您没中奖！")
        return 0
    #end_list = sorted(list(list1[0])) + sorted(list(list1[1]))
    #return end_list


def rand():
    str_num = ''
    list1 = [[],[]]
    while len(list1[0]) < 5:
        list1[0] = set(list1[0])
        a = random.randint(1, 36)
        list1[0].add(a)
        list1[0] = set(list1[0])

    while len(list1[1]) < 2:
        list1[1] = set(list1[1])
        a = random.randint(1, 13)
        list1[1].add(a)
        list1[1] = set(list1[1])
    end_list = list(list1[0])+list(list1[1])
    for i in end_list:
        str_num = str_num + str(i)
        if i == 6:
            pass
        else:
            str_num = str_num + ' '
    return str_num
print("开奖号码为：")


list1 = []
for i in range(10):
    str1 = rand()
    list1.append(daletou(str1))

list2 = []
for p in range(1):
    c = 0
    for q in list1:
        if q==p:
            c+=1
    list2.append(c)
print(list2)
time.sleep(10)