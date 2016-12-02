#!/usr/bin/env python
# -*- conding:utf-8 -*-
# Author: dengliping
DICT = {'dengliping':'123','laotian':'456'}
LIST = []
FLAG = True
while FLAG:
    NUM = 0
    name = input('请输入你的用户名:')
    if name in DICT and name not in LIST:
        while FLAG:
            password = input('请输入你的密码:')
            if password == DICT[name]:
                print('欢迎光临')
                exit()
            elif NUM == 2:
                print('用户将会锁定')
                LIST.append(name)
                break
            else:
                NUM += 1
                print('密码或用户名错误')
    else:
        print('你输入错误 请重新输入！')