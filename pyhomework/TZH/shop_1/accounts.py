#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import time
import os
import shutil
import shop_run
import cost

BUY_GOOD = {}

def settle():
    d_count = 1
    shop_run.judge()
    if os.path.exists('shop_goods.conf'):
        ft,salary,user_salary = cost.price()
        if ft:
            print ('您的资金充足，正在进行结算，请稍后。。。')
            time.sleep(3)
            shutil.copy('user.conf','user.conf.back')
            residue_salary = salary - user_salary
            with open('user.conf','r') as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    if line.strip() == '[购物车商品]':
                        start_count = line_count
                    elif line.strip() == '[历史信息]':
                        end_count = line_count
            with open('user.conf.back','r') as f1, open('user.conf','w') as f2:
                user_count = 0
                for line in f1:
                    user_count += 1
                    if line.count('\n') == len(line):
                        f2.write(line)
                    elif user_count == 1:
                        f2.write('|'.join([line.strip().split('|')[0],line.strip().split('|')[1],str(residue_salary)])+'\n')
                    elif start_count < user_count < end_count - 1:
                        BUY_GOOD[d_count] = [line.strip(),time.asctime()]
                        d_count += 1
                    else:
                        f2.write(line)
            shutil.copy('user.conf','user.conf.back')
            with open('user.conf.back','r') as f1, open('user.conf','w') as f2:
                for line in f1:
                    f2.write(line)
                for key in BUY_GOOD:
                    f2.write(','.join([BUY_GOOD[key][0],BUY_GOOD[key][1]])+'\n')
            print ('您的消费金额为{}元，账户余额为{}元'.format(user_salary,residue_salary))
            exit()
        else:
            print '您的账户余额不足，，请充值后再进行结账。。。'
            time.sleep(2)
    else:
        print ('没有购买任何物品，。。')