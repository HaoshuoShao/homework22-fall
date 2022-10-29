#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：邵豪硕
# 创建：2022-10-10
# 更新：2022-10-25
# 作用：定义了用于读写物品信息的类以及读写方法

import csv
import os



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

    def WriteGoodInfo(self):
        if not os.path.exists('./DATA.csv'):
            with open('./DATA.csv', mode='w', newline='') as f:
                dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataWriter.writerow(['index', 'goods', 'provider', 'time', 'amount', 'isChanged', 'des'])


        with open('./DATA.csv', newline='') as f:
            dataReader = csv.reader(f, delimiter=',')
            goodsNum = 0
            for line in dataReader:
                if line:
                    goodsNum += 1

        with open('./DATA.csv', mode='a+', newline='') as f:
            dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
            if goodsNum:
                dataWriter.writerow([goodsNum, self.GetGoods(), self.GetProvider(), self.GetTime(), 
                                     self.GetAmount(), self.GetIsChanged(), self.GetDes()])
                
            else:
                
                dataWriter.writerow([goodsNum, self.GetGoods(), self.GetProvider(), self.GetTime(), 
                                     self.GetAmount(), self.GetIsChanged(), self.GetDes()])
                                     

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
