#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import shutil
import shop_run

TAG = True
DICT_GOOD = {}

def cart():
    while TAG:
        COUNT = 0
        shop_run.judge()
        count = 1
        shutil.copy('user.conf','user.conf.back')
        f = open('user.conf','r')
        for line in f:
            if line.strip() == '[购物车商品]':
                star_count = count
            elif line.strip() == '[历史信息]':
                end_count = count
            count += 1
        f.close()
        print ('已加入购物车的商品有:')
        with open('user.conf.back','r') as f1:
            shop_count = 0
            for line in f1:
                shop_count += 1
                if shop_count == 4 and line.count('\n') == len(line):
                    print ('没有选择任何商品。。。')
                    return
                elif star_count < shop_count < end_count:
                    if line.count('\n') == len(line):
                        continue
                    else:
                        COUNT += 1
                        print COUNT,'---',line.strip()
                        DICT_GOOD[str(COUNT)] = line.strip()
                else:
                    continue
        cart_choice = raw_input('请选择购物车的操作功能(c=clear/d=delete/p=pass):'.strip().lower())
        if cart_choice == 'd':
            while TAG:
                del_choice = raw_input('请输入您要删除的商品序号（单项选择删除):')
                if del_choice.isdigit() and 0 < int(del_choice) <= COUNT:
                    shutil.copy('user.conf','user.conf.back')
                    with open('user.conf','r') as f:
                        count = 1
                        for line in f:
                            if line.strip() == '[购物车商品]':
                                star_count = count
                            elif line.strip() == '[历史信息]':
                                end_count = count
                            count += 1
                        with open('user.conf.back', 'r') as f1, open('user.conf', 'w') as f2:
                            shop_count = 0
                            yn = 0
                            for line in f1:
                                shop_count += 1
                                if line.count('\n') == len(line):
                                    f2.write(line)
                                elif star_count < shop_count < end_count:
                                    if line.strip() == DICT_GOOD[del_choice] and yn == 0:
                                        yn += 1
                                        continue
                                    else:
                                        f2.write(line)
                                else:
                                    f2.write(line)
                            break
                else:
                    print('您输入的有误，请重新输入')
        elif cart_choice == 'p':
            return
        elif cart_choice == 'c':
            shutil.copy('user.conf', 'user.conf.back')
            f = open('user.conf', 'r')
            count = 1
            for line in f:
                if line.strip() == '[购物车商品]':
                    star_count = count
                elif line.strip() == '[历史信息]':
                    end_count = count
                count += 1
            f.close()
            print ('已加入购物车的商品有:')
            with open('user.conf.back', 'r') as f1, open('user.conf','w') as f2:
                shop_count = 0
                for line in f1:
                    shop_count += 1
                    if line.count('\n') == len(line):
                        f2.write(line)
                    elif star_count < shop_count < end_count:
                        continue
                    else:
                        f2.write(line)
            print ('购物车已经清空')
            return
        else:
            print ('您输入的有误，请重试')
    shop_run.code()