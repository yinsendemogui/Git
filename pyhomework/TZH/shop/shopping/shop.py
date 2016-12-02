#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os

TAG = True

GOODS = {'1':['IPHONE',5888],'2':['电视机',3999],'3':['IPAD  ',2998],'4':['空调  ',2199],
         '5':['洗衣机',1588],'6':['脚踏车',998],'7':['电暖器',588],'8':['加湿器',199]}

def trade():
    if  not os.path.exists('shop.conf'):
        f = open('shop.conf','w')
        for i in xrange(1,9):
            i = str(i)
            f.write('*'.join([i,GOODS[i][0],str(GOODS[i][1])])+'\n')
        f.close()

    f = open('shop.conf','r')
    for line in f:
        good = line.strip().split('*')
        print good[0],'.','---',good[1],'------',good[2]
    f.close()