#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import shutil
import shop_run

GOOD_DICT = {'1':['IPHONE',5888],'2':['电视机',3999],'3':['IPAD  ',2998],'4':['空调  ',2199],
         '5':['洗衣机',1588],'6':['脚踏车',998],'7':['电暖器',588],'8':['加湿器',199]}

TAG = True
SIGN_1 = '[购物车商品]'
SIGN_2 = '[历史信息]'

def trade():
    shop_run.judge()
    if not os.path.exists('shop_goods.conf'):
        f = open('shop_goods.conf','w')
        for i in xrange(1,9):
            row = str(i)
            f.write(','.join([row,GOOD_DICT[row][0],str(GOOD_DICT[row][1])])+'\n')
        f.close()
    f = open('shop_goods.conf', 'r')
    for line in f:
        print line.strip()
    f.close()
    shop_run.code()
    while TAG:
        good_choice = raw_input('请输入您选择购买的商品(可同时多项选择):')
        if set(good_choice) <= set('12345678'):
            shop_run.judge()
            f = open('user.conf','r')
            lines_count = 0
            for line in f:
                lines_count += 1
                if line.strip() == SIGN_2:
                    end_count = lines_count
            f.close()
            shutil.copy('user.conf','user.conf.back')
            with open('user.conf.back','r') as f1, open('user.conf','w') as f2:
                end_line = end_count - 1
                cart_count = 1
                for line in f1:
                    if cart_count == end_line - 1:
                        f = open('shop_goods.conf','r')
                        for lines in f:
                            for goods in good_choice:
                                if lines.split(',')[0] == goods:
                                    f2.write(lines.split(',')[1].strip()+'\n')
                        f2.write('\n')
                    else:
                        f2.write(line)
                    cart_count += 1
            shop_run.code()
            return
        else:
            print ('无此商品，请重试')