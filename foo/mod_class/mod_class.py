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

        #self.index = 0  #TODO 读取csv文件，分配物品编号
    
    #TODO 按照物品编号访问csv文件，读取对应物品信息
    def ReadGoodInfo(self, index):
        
        
        return 

    #TODO 将物品信息写入csv文件
    def WriteGoodInfo(self):

    
