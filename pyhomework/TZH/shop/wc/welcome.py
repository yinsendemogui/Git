#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import random

LIST = ['1', '2', '3', '4', '5','6']
choice_1 = {'1':'  购物  ','2':' 购物车 ','3':'  结账  ','4':'历史纪录',
          '5':'网上银行','6':'退出'}

def wlc(user,salary):
    print ('{0},欢迎光临ABC商城，您的账户余额为{1}元'.format(user, salary).center(100, '-'))
    for key in LIST:
        print key,choice_1[key].center(50,'*')