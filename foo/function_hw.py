import csv

import class_hw


# 清空重置csv文件
def clearItem():
    with open('./docs/DATA.csv', mode='w', newline='') as f:
        dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dataWriter.writerow(['index', 'goods', 'provider', 'time', 'amount', 'isChanged', 'des'])


# 添加物品条目进入csv文件
def AddItem(goods, provider, time, amount, isChanged, des):
    newGoodInfo = class_hw.GoodInformation(goods, provider, time, amount, isChanged, des)
    newGoodInfo.WriteGoodInfo()


# 删除物品条目从csv文件中
def DeleteItem(index):
    index = index - 1
    with open('./docs/DATA.csv', newline='') as f:
        data = [row for row in csv.DictReader(f)]
    
    with open('./docs/DATA.csv', mode='w', newline='') as f:
        dataWriter = csv.writer(f)
        
        if (index >= csv.reader(f).line_num) or (data[index]['isChanged'] == 'True'):
            print("无此项或已删除")
            return
        
        data[index]['isChanged'] = 'True'

        dataWriter.writerow(['index', 'goods', 'provider', 'time', 'amount', 'isChanged', 'des'])
        for line in data:
            dataWriter.writerow(list(line.values()))
        

# 显示物品列表
def ShowItems():
    with open('./docs/DATA.csv', newline='') as f:
        dataReader = csv.DictReader(f)

        print("物品信息列表如下：")
        for line in dataReader:
            if line['isChanged'] == 'False':
                print(line)


# 根据关键字查询物品
def queryItem(query):
    with open('./docs/DATA.csv', newline='') as f:
        dataReader = csv.DictReader(f)

        print("发现包含", end=' ')
        print(query,end=' ')
        print("的内容如下：")

        for line in dataReader:
            if (line['isChanged'] == 'False') and (query in line['goods']):
                print(line.values())
