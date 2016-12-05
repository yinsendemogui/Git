#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import shutil
import shop_run
import time

def bank():
    shop_run.judge()
    shutil.copy('user.conf','user.conf.back')
    with open('user.conf','r') as f:
        u_count = 1
        for line in f:
            if u_count == 1:
                salary = int(line.split('|')[2])
                u_count += 1
    input_money = raw_input('您的账户余额为{}元，请输入要充值的金额(q=quit)：'.format(salary))
    if input_money == 'q':
        return
    elif input_money.isdigit():
        print ('正在充值，请稍后。。。')
        time.sleep(2)
        new_salary = salary + int(input_money)
        u_count = 1
        with open('user.conf.back','r') as f1, open('user.conf','w') as f2:
            for line in f1:
                if u_count == 1:
                    f2.write('|'.join([line.split('|')[0],line.split('|')[1],str(new_salary)]))
                    f2.write('\n')
                    u_count += 1
                else:
                    f2.write(line)
    print ('您充值后的金额为{}元'.format(new_salary))