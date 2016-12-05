#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian

LIST = ['1','2','3','4','5','6']
SHOP_FUNCTION = {'1':'  购物  ','2':' 购物车 ','3':'  结账  ',
                 '4':'历史记录','5':'  充值  ','6':'  退出  '}


def welcome():
    for key in LIST:
        print key,SHOP_FUNCTION[key].center(50,'*')