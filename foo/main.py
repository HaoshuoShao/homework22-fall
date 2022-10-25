#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：邵豪硕
# 创建：2022-10-10
# 更新：2022-10-23
# 作用：存储修改居民用于交换的物品信息

import os
import sys
import time

import function_hw as F

while 1:

    print("输入数字选择对应操作：")
    print("1. 添加物品信息")
    print("2. 删除物品信息")
    print("3. 显示物品列表")
    print("4. 查找物品信息")
    print("5. 退出程序")

    optIndex = input()

    # 操作选项
    if optIndex == '1':
        print("依次输入物品名称，提供者，数量，备注信息，以空格分隔")
        
        # 获取时间
        getTime = time.localtime(time.time())
        getDate = str(getTime.tm_year) + '/' + str(getTime.tm_mon) + '/' + str(getTime.tm_mday)

        isChanged = False

        goods, provider, amount, des = (input().split())

        F.AddItem(goods, provider, time, amount, isChanged, des)

    elif optIndex == '2':
        print("需要删除的物品编号:")
        index = int(input())
        F.DeleteItem(index)

    elif optIndex == '3':
        F.ShowItems()

    elif optIndex == '4':
        print("需要查询的物品包含字段:")
        query = input()
        F.QueryItem(query)

    elif optIndex == '5':
        sys.exit()

    else:
        next
    
    print("输入回车继续")
    input()



