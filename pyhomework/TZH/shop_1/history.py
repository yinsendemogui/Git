#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import shop_run
import shutil
import time

def past():
    shop_run.judge()
    shutil.copy('user.conf','user.conf.back')
    f = open('user.conf','r')
    count_1 = 0
    for line in f:
        count_1 += 1
        if line.strip() == '[历史信息]':
            start_count = count_1
    f.close()
    print ('您以往购买的商品有：')
    with open('user.conf','r') as f1:
        COUNT = 1
        count_2 = 0
        for line in f1:
            count_2 += 1
            if count_2 > start_count:
                print ('{},商品:{}\t购买日期:{}'.format(COUNT,line.split(',')[0],line.split(',')[1]))
                time.sleep(0.5)
                COUNT += 1
    print ('您共购买{}件商品'.format(COUNT - 1))
    shop_run.code()