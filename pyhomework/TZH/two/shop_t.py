#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian

USER_GOODS = []
DB = [True]
TAG = True
COUNT = 1
MONEY = 0
USER_MSG = {'tian':['qq123',0],'rong':['qq123',0],'you':['qq123',0]}
GOODS_1 = {'1':'手机','2':'运动',"3":'黄金'}
GOODS_2 = {'手机':{'1':['Iphone    ',5188],'2':['Samsung   ',3888],'3':['OPPO      ',2999],'4':['MI        ',1999]},
           '运动':{'1':['Treadmill ',2499],'2':['SPINNING  ',1398],'3':['Basketball',599,],'4':['Football  ',199]},
           '黄金':{'1':['Necklace  ',15000],'2':['Bracelet  ',8888],'3':['Earrings  ',3000],'4':['Ring      ',1500]}}

def Recharge():         #判断余额，是否需要充值
    while TAG:
        m_choice = raw_input('您的余额不足，是否充值，否则无法购买商品(y/n) q="quit":')
        if m_choice.strip().lower() == 'y':
            while TAG:
                in_salary = raw_input('请输入您要充值的金额:')
                if in_salary.isdigit():
                    in_salary = int(in_salary)
                    USER_MSG[user][1] += in_salary
                    print ('{},您的余额为{}元'.format(user, USER_MSG[user][1]))
                    return
                else:
                    print('请输入正确的金额！')
        elif m_choice.strip().lower() == 'n':
            print('您的余额是{}元，'.format(USER_MSG[user][1]))
            break
        elif m_choice.strip().lower() == 'q':
            print('欢迎下次光临，再见')
            exit()
        else:print('没有此选项，请仔细阅读。。')

def Goods_choice():     #判定多选，是否继续
        if len(y_choice) == len(set(y_choice)) and set(y_choice) <= set('1234'):
            DB[0] = [False]
            return
        elif len(y_choice) != len(set(y_choice)) and set(y_choice) <= set('1234'):
            while TAG:
                tf_choice = raw_input('您的选择有重复，是否确认购买(y/n):')
                if tf_choice[0].strip().lower() == 'y':
                    DB[0] = [False]
                    return
                elif tf_choice[0].strip().lower() == 'n':
                    break
                else:print('您输入的有误，重新确认')
        else:
            print('超标，，请重试')


print('Welcome to ABC Shopping Mall'.center(100, '-'))
while TAG:
    user = raw_input("请输入您的用户名: ")
    passwd = raw_input('请输入您的密码: ')
    if user in USER_MSG and USER_MSG[user][0] == passwd:
        print('欢迎，{},您的账户余额为{} 元！'.format(user,USER_MSG[user][1]))
        if USER_MSG[user][1] < 199:
            Recharge()
        while TAG:
            for i in ['1','2','3']:
                print i,'--------',GOODS_1[i]
            choice = raw_input('请选择购物的种类(1/2/3)or q = "quit:')
            if choice == 'q':
                exit()
            elif choice in ['1','2','3']:
                while TAG:
                    for i in ['1', '2', '3', '4']:
                        print i, '---', GOODS_2[GOODS_1[choice]][i][0], '------', GOODS_2[GOODS_1[choice]][i][1]
                    y_choice = raw_input('请选择您需要的商品(可多选1/2/3/4,q="quit",b="back"):')
                    if y_choice[0].strip().lower() == 'q': exit()
                    elif y_choice[0].strip().lower() == 'b':break
                    else:
                        Goods_choice()
                        if DB[0] is not True:break
                        else:print('请重新选择。。')
                print('您购买的商品是：')
                for good in y_choice:
                    DB[0] = True
                    print COUNT,'.',GOODS_2[GOODS_1[choice]][good][0]
                    USER_GOODS.append(GOODS_2[GOODS_1[choice]][good][0])
                    MONEY += GOODS_2[GOODS_1[choice]][good][1]
                    COUNT += 1
                print ('共花费{}元'.format(MONEY))
                while TAG:
                    c_choice = raw_input('是否继续购买(y/n):'.strip().lower())
                    if c_choice[0] == 'y':break
                    elif c_choice[0] == 'n':
                        while TAG:
                            if MONEY > USER_MSG[user][1]:
                                Recharge()
                            else:
                                COUNT = 1
                                print('您购买的商品有:')
                                for goods in USER_GOODS:
                                    print COUNT, '.',goods
                                    COUNT += 1
                                print ('您的余额为{}元.谢谢您的光临，再见。。'.format(USER_MSG[user][1]-MONEY))
                                exit()
                    else:print('输入有误，请重试。。')
            else:
                print('您输入的有误，请重新选择。')
    else:
        print("您输入的用户名或密码错误，请重新输入。。。")