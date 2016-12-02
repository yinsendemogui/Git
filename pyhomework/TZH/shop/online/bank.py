#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import shutil

TAG = True

def money():
    print ('欢迎光临网上银行'.center(60,'*'))
    shutil.copy('user.conf', 'user.conf.bak')
    f1 = open('user.conf.bak','r')
    for line in f1:
        print ('您的账户金额为{}元'.format(line.split('|')[2]))
    f1.close()
    while TAG:
        io_money = raw_input('是否进行充值(y/n):')
        if io_money == 'y':
            while TAG:
                in_money = raw_input('请输入您要充值的金额:')
                if in_money.isdigit():
                    with open('user.conf.bak','r') as f1, open('user.conf','w') as f2:
                        for line in f1:
                            mon = int(line.split('|')[2].strip()) + int(in_money)
                            f2.write('|'.join([line.split('|')[0],line.split('|')[1],str(mon)]))
                    print ('充值已成功，充值后金额为{}元'.format(mon))
                    break
                else:
                    print ('输入正确的金额，，')
        elif io_money == 'n':
            return
        else:
            print ('您的选择有误，请重新进行选择')
