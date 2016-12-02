#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
TAG = True

def degress(gs):
    while TAG:
        f = open('user.conf','r')
        sy = f.read()
        salary = int(sy.split('|')[2])
        f.close()
        if salary >= gs:
            return True
        else:
            return False