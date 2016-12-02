#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import time
from costing import cost
import shutil
import time

TAG = True
list_h = []

def sa():
    SALARY = 0
    if os.path.exists('shop.conf'):
        f = open('shop.conf','r')
        shutil.copy('shopcart.conf','shopcart.conf.bak')
        for lineses in f:
            with open('shopcart.conf.bak', 'r') as t1, open('shopcart.conf', 'w') as t2:
                for lines in t1:
                    if lineses.split('*')[0] == lines.split(',')[0]:
                        SALARY += int(lineses.split('*')[2])
                        ft = os.path.exists('history.conf')
                        if not ft:
                            q = open('history.conf', 'w')
                            q.write('|'.join([lineses.split('*')[1]])+'\n')
                            q.close()
                        else:
                            shutil.copy('history.conf','history.conf.bak')
                            with open('history.conf.bak','r') as h1, open('history.conf','w') as h2:
                                for line in h1:
                                    h2.write(line)
                                h2.write('|'.join([lineses.split('*')[1]])+'\n')
                    else:
                        continue
        f.close()
        if cost.degress(SALARY):
            shutil.copy('user.conf','user.conf.bak')
            with open('user.conf.bak','r') as f1, open('user.conf','w') as f2:
                for line in f1:
                    salary = line.split('|')[2]
                    salary = int(salary) - SALARY
                    f2.write('|'.join([line.split('|')[0],line.split('|')[1],str(salary)]))
            js = 1
            print ('您本次购买的商品有：')
            f = open('shopcart.conf.bak','r')
            for good in f:
                print js,'---',good.split(',')[1].strip()
                js += 1
            print ('您的消费金额为{}元，余额为{}元'.format(SALARY,salary))
            exit()
        else:
            print ('您的余额不足，请充值或进入购物车进行删除商品')
    else:
        print ('对不起，您没有选购任何物品')
        return