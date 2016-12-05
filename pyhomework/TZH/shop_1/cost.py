#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
# 成本核算
import shop_run
import os

def price():
    s_count = 1
    shop_run.judge()
    if os.path.exists('shop_goods.conf'):
        f = open('user.conf', 'r')
        count = 1
        for line in f:
            if s_count == 1:
                aa = line.strip().split('|')
                salary = int(aa[2])
            elif line.strip() == '[购物车商品]':
                    start_count = count
            elif line.strip() == '[历史信息]':
                    end_count = count
            s_count += 1
            count += 1
        f.close()
        with open('user.conf','r') as f1:
            user_salary = 0
            shop_count = 0
            for line in f1:
                shop_count += 1
                if start_count < shop_count < end_count:
                    with open('shop_goods.conf','r') as f2:
                        for lines in f2:
                            if line.strip() == lines.split(',')[1].strip():
                                user_salary += int(lines.strip().split(',')[2])
        if salary >= user_salary:
            return (True,salary,user_salary)
        else:
            return (False,salary,user_salary)
    else:
        return