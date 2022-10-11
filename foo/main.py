import os
import sys

import function_hw as F

while 1:
    # 打印操作提示
    print("输入数字选择对应操作：")
    print("1. 添加物品信息")
    print("2. 删除物品信息")
    print("3. 显示物品列表")
    print("4. 查找物品信息")
    print("5. 退出程序")

    # 输入操作
    optIndex = input()

    # 操作选项
    if optIndex == '1':
        print("物品名称:")
        goods = input()
        print("提供者:")
        provider = input()
        print("发布时间:")
        time = input()
        print("数量:")
        amount = input()
        isChanged = 'False'
        print("备注:")
        des = input()
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
        F.queryItem(query)

    elif optIndex == '5':
        sys.exit()

    else:
        next
    
    print("输入任意字符继续")
    input()
    os.system('cls')



