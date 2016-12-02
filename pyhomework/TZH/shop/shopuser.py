#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import random
import shutil
#from shop.shopping import shop
from shopping import shop
from wc.welcome import wlc
from costing import cost
from shopcar import shopcart
from settle import accounts
from history import past
from online import bank

def contrast():
    if not os.path.exists('shopcart.conf'):
        f = open('shopcart.conf', 'w')
        for line in f4:
            for i in sc:
                if line.split('*')[0] == i:
                    f.write(','.join([i, line.split('*')[1]]) + '\n')
        f4.close()
        f.close()
    else:
        shutil.copy('shopcart.conf', 'shopcart.conf.bak')
        with open('shopcart.conf.bak', 'r') as f1, open('shopcart.conf', 'w') as f2:
            for line in f1:
                f2.write(line.strip() + '\n')
            for line in f4:
                for i in sc:
                    if line.split('*')[0] == i:
                        f2.write(','.join([i, line.split('*')[1]]) + '\n')
            f4.close()

TAG = True
COUNT = 1
LIST = []
SALARY = 0

while TAG:
    user = raw_input('请输入您的用户名：')
    pwd = raw_input('请输入您的密码：')
    # while TAG:
    #     li = []
    #     for i in xrange(6):
    #         r = random.randrange(1,7)
    #         if r == 2 or r ==4:
    #             a = random.randrange(0,9)
    #             li.append(str(a))
    #         elif r == 1 or r == 5:
    #             b = random.randrange(65,90)
    #             li.append(chr(b))
    #         else:
    #             c = random.randrange(97,122)
    #             li.append(chr(c))
    #     yzm = ''.join(li)
    #     yan = raw_input('请输入验证码({})\n '.format(yzm))
    #     if yan == yzm:
    #         break
    #     else:
    #         print('验证码错误，请重新输入')
    if not os.path.exists('user.conf'):
        f = open('user.conf','w')
        while TAG:
            salary = raw_input('欢迎首次登录，请输入您的工资金额：')
            if salary.isdigit():
                break
            else:
                print('您输入的金额有误，请正确输入')
        f.write('|'.join([user,pwd,salary]))
        f.close()
        break
    else:
        f = open('user.conf','r')
        local_user = f.read()
        use = local_user.split('|')
        if use[0] == user and use[1] == pwd:
            salary = int(use[2])
            f.close()
            break
        else:
            print('您输入的用户或密码错误，请重新确认。。')

while TAG:
    wlc(user, salary)
    choice = raw_input('请输入您需要的功能(1/2/3/4/5/6):')
    if choice == '1':
        shop.trade()
        f = open('shop.conf','r')
        while TAG:
            good_choice = raw_input('请输入您需要的物品(可多选):')
            if set(good_choice) <= set('12345678'):
                sc = list(good_choice)
                print('您选择的商品为：')
                for line in f:
                    for i in sc:
                        if i == line.split('*')[0]:
                            print COUNT,'---',line.split('*')[1]
                            type(SALARY)
                            SALARY += int(line.split('*')[2])
                            COUNT += 1
                        else:
                            pass
                COUNT = 1
                break
            else:
                print('输入错误，无此商品。')
        f4 = open('shop.conf','r')
        if cost.degress(SALARY):
            contrast()
        else:
            print('您的余额不足，请届时充值')
            contrast()
    elif choice == '2':
        shopcart.cart()
    elif choice == '3':
        accounts.sa()
    elif choice == '4':
        past.ifmt()
    elif choice == '5':
        bank.money()
    elif choice == '6':
        exit()
    else:
        print('请仔细阅读，谨慎选择，谢谢。。')