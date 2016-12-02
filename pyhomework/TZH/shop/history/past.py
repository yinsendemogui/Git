#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import time
import os

def ifmt():
    if os.path.exists('history.conf'):
        cc = 0
        print ('您购买的历史物品有：')
        f = open('history.conf','r')
        for line in f:
            cc += 1
            print cc,'------',line.strip()
        print ('共{}件商品'.format(cc))
        time.sleep(3)
    else:
        print ('没有购物记录，欢迎购买')