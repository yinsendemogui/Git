#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import shutil
from costing import cost

TAG = True
DICT = {}
LIST_CART = []
LIST_COUNT = []
S = 0

def cart():
    while TAG:
        SALARY = 0
        COUNT = 1
        if os.path.exists('shopcart.conf'):
            f = open('shopcart.conf','r')
            for line in f:
                print COUNT,'------',line.split(',')[1].strip()
                DICT[COUNT] = line.split(',')[1].strip()
                LIST_COUNT.append(str(COUNT))
                COUNT += 1
            f.close()
            p = open('shop.conf', 'r')
            for li in p:
                f = open('shopcart.conf', 'r')
                for line in f:
                    if li.split('*')[0] == line.split(',')[0]:
                        SALARY += int(li.split('*')[2])
                    else:continue
                f.close()
            p.close()
            if COUNT-1 == 0:
                print('无任何商品，。。')
                return
            print ('您本次共购买了{}件商品,需要消费{}元'.format(COUNT-1,SALARY))
            ff = cost.degress(SALARY)
            if ff:print('您的资金充足')
            else:print('您的资金不足，请届时充值')
            cart_choice = raw_input('请选择购物车的操作功能(c=clear/d=delete/p=pass):'.strip().lower())
            if cart_choice == 'd':
                while TAG:
                    del_choice = raw_input('请输入您要删除的商品序号（单项选择删除):')
                    if del_choice.isdigit() and int(del_choice) <= COUNT-1:
                        shutil.copy('shopcart.conf','shopcart.conf.bak')
                        with open('shopcart.conf.bak','r') as f1, open('shopcart.conf','w') as f2:
                            count = 0
                            f3 = open('shop.conf', 'r')
                            for line in f1:
                                if line.split(',')[1].strip() != DICT[int(del_choice)]:
                                    f2.write(','.join([line.split(',')[0],line.split(',')[1]]))
                                    for lines in f3:
                                        lines.split('*')[1] == line.split(',')[1]
                                        SALARY += int(lines.split('*')[2])
                                else:
                                    if count == 0:
                                        count = 1
                                        continue
                                    else:
                                        f2.write(','.join([line.split(',')[0], line.split(',')[1]]))
                                        for lines in f3:
                                            lines.split('*')[1] == line.split(',')[1]
                                            SALARY += int(lines.split('*')[2])
                            f3.close()
                            break
                    else:
                        print('您输入的有误，请重新输入')
            elif cart_choice == 'p':
                return
            elif cart_choice == 'c':
                f = open('shopcart.conf','w')
                f.close()
                print ('购物车已经清空')
                return
            else:
                print ('您输入的有误，请重试')
        else:
            print ('购物车空，请进行购物')
            return