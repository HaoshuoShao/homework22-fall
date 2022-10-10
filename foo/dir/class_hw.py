import os
import csv

# GoodInformation类用于存储物品信息
class GoodInformation:

    goods = "" 
    provider = ""
    time = ""
    amount = ""
    isChanged = False
    des = ""
    
    def __init__(self, goods, provider, time, amount, isChanged, des):
        
        self.goods = goods
        self.provider = provider
        self.time = time
        self.amount = amount
        self.isChanged = isChanged
        self.des = des

    # 将物品信息写入csv文件
    def WriteGoodInfo(self):
        with open('./docs/DATA.csv', mode='a', newline='') as dataFile:
            dataReader = csv.reader(dataFile, delimiter=',')
            dataWriter = csv.writer(dataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            goodNum = dataReader.line_num

            if goodNum:
                dataWriter.writerow([self.GetGoods, self.GetProvider, self.GetTime, 
                                     self.GetAmount, self.GetIsChanged, self.GetDes])
            else:
                dataWriter.writerow(['goods', 'provider', 'time', 'amount', 'isChanged', 'des'])

    # 访问物品信息
    def GetGoods(self):
        return self.goods

    def GetProvider(self):
        return self.provider

    def GetTime(self):
        return self.time

    def GetAmount(self):
        return self.amount

    def GetIsChanged(self):
        return self.isChanged

    def GetDes(self):
        return self.des
