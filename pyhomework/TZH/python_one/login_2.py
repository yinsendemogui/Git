#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
TAG = True
USER = {'tian':'qq123','rong':'qq123','hao':'qq123'}
LOCK = []

while TAG:
    COUNT = 0
    user = raw_input('Pls input your name:  ')
    if user in LOCK:
        print 'jiujiu ..gun'
        exit()
    elif user in USER:
        while TAG:
            passwd = raw_input('Pls input your password:  ')
            if passwd == USER[user]:
                print 'haha...Welcome {}'.format(user)
                break         ###错了，
            elif COUNT == 2:
                print '悠悠，，再见'
                LOCK.append(user)
                break
            else:
                print 'Error input ,Pls try again'
                COUNT += 1
    else:
        print '无此用户！'