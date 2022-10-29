#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：邵豪硕
# 创建：2022-10-10
# 更新：2022-10-25
# 作用：定义“添加物品条目进入csv文件” “删除物品条目从csv文件中” 
# “显示物品列表” “根据关键字查询物品” “清空重置csv文件” 等操作指令

import csv
import os
import time
import class_hw


def ClearItem():
    with open('./docs/DATA.csv', mode='w', newline='') as f:
        dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dataWriter.writerow(['index', 'goods', 'provider', 'time', 'amount', 'isChanged', 'des'])


def AddItem(goods, provider = '', amount = '', isChanged = False, des = ''):
    # 获取时间
    getTime = time.localtime(time.time())
    getDate = str(getTime.tm_year) + '/' + str(getTime.tm_mon) + '/' + str(getTime.tm_mday)
    newGoodInfo = class_hw.GoodInformation(goods, provider, getDate, amount, isChanged, des)
    newGoodInfo.WriteGoodInfo()


def DeleteItem(index):

    with open('./docs/DATA.csv', newline='') as f:
        data = []
        goodsNum = 0

        #计算csv文件条目数量，因为csv.line_num有问题
        for row in csv.DictReader(f):   
            data.append(row)
            goodsNum += 1

        #判断删除项是否已经被删除/下标越界
        if (index > goodsNum) or (data[index - 1]['isChanged'] == 'True'): 
            print(goodsNum)
            print("无此项或已删除")

            return
    
    with open('./docs/DATA.csv', mode='w', newline='') as f:
        dataWriter = csv.writer(f)
        
        data[index - 1]['isChanged'] = 'True'

        dataWriter.writerow(['index', 'goods', 'provider', 'time', 'amount', 'isChanged', 'des'])
        for line in data:
            dataWriter.writerow(list(line.values()))

        print("第%s项物品已删除"%index)

        

def ShowItems():
    if not os.path.exists('./docs/DATA.csv'):
        print("没有记录的物品信息")
        return
    
    with open('./docs/DATA.csv', newline='') as f:
        dataReader = csv.DictReader(f)

        print("物品信息列表如下：")
        for line in dataReader:
            if line['isChanged'] == 'False': #不显示已被删除的条目
                print(line)


def QueryItem(query):
    if not os.path.exists('./docs/DATA.csv'):
        print("没有记录的物品信息")
        return

    with open('./docs/DATA.csv', newline='') as f:
        dataReader = csv.DictReader(f)

        print("发现包含", end=' ')
        print(query,end=' ')
        print("的内容如下：")

        for line in dataReader:
            if (line['isChanged'] == 'False') and (query in line['goods']):
                print(line.values())
