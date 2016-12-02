#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:dengliping
salary = {'dengliping':1000000,'laotian':100000}
shop_car = []
userdict = {'dengliping':'123456','laotian':'666666'}
admindict = {'admin':'time.9818'}
Welcome_msg = 'Welcome to shopping'.center(50,'-')
# shopping_list = {'手机类':{'iphone':'5299','sumsing':'6199','xiaomi':'2099'},
#                  '电脑类':{'thinkpad':'7999','mac':'10999','waixingren':'19999'}}
shopping_list = {'手机类':[('iphone',5299),('sumsing',6199),('xiaomi',2099)],
                 '电脑类':[('thinkpad',7999),('mac',10999),('waixingren',19999)]}
shopping_list1 = {1:'手机类',2:'电脑类',3:'充值'}
Flag = True
print(Welcome_msg)
while Flag:
    userip1 = input("请输入你的用户名:")
    if userip1 in userdict:
        userip2 = input("请输入你的密码:")
        if userip2 == userdict[userip1]:
            print('欢迎光临，{}你的余额为{}'.format(userip1,salary[userip1]))
            print(Welcome_msg)
            #print ('1.{0}\n''2.{1}\n''3.{2}'.format(shopping_list1[1],shopping_list1[2],shopping_list1[3]))
            while Flag:
                print('1.{0}\n''2.{1}\n''3.{2}'.format(shopping_list1[1],shopping_list1[2],shopping_list1[3]))
                usershop = input("输入'123','q/b退出'请选择你要购买的商品种类：")
                if usershop == '1':
                    # print(shopping_list[shopping_list1[1]])
                    for item in enumerate(shopping_list[shopping_list1[1]]):
                        index = item[0]
                        p_name = item[1][0]
                        p_price = item[1][1]
                        print(index, '.', p_name, p_price)
                    usershop1 = input(",选择要购买的商品，q/b退出:")
                    usershop1 = int(usershop1)
                    if usershop1 < len(shopping_list[shopping_list1[1]]):
                        p_item = shopping_list[shopping_list1[1]][usershop1]
                        salary1 = int(salary[userip1])
                    if p_item[1] <= salary1:
                        shop_car.append(p_item)
                        salary1 -= p_item[1]
                        print('购买商品{}，你的余额为{}'.format(p_item,salary1))
                    else:
                        print('你的余额不足{}，请充值'.format(salary1))
                elif usershop == '2':
                        for item in enumerate(shopping_list[shopping_list1[2]]):
                            index1 = item[0]
                            p_name1 = item[1][0]
                            p_price1 = item[1][1]
                            print(index1, '.', p_name1, p_price1)
                        usershop2 = input(",选择要购买的商品，q/b退出:")
                        usershop2 = int(usershop2)
                        if usershop2 < len(shopping_list[shopping_list1[2]]):
                            p_item2 = shopping_list[shopping_list1[2]][usershop2]
                            salary2 = int(salary[userip1])
                        if p_item2[1] <= salary2:
                            shop_car.append(p_item2)
                            salary2 -= p_item2[1]
                            print('购买商品{}，你的余额为{}'.format(p_item2,salary2))
                        else:
                            print('你的余额不足{}，请充值'.format(salary2))
                elif usershop == '3':
                    userip3 = input('请输入管理员账户:')
                    if userip3 == 'admin':
                        userip4 = input("请输入你的密码:")
                        if userip4 == admindict[userip3]:
                            print('{}登录成功！'.format(userip3))
                            admin1 = input('请选择需要充值的用户:')
                            if admin1 in userdict:
                                admin2 = input('请输入是需要充值的金额：')
                                admin2 = int(admin2)
                                #salary[admin1] + admin2= salary[admin1]# 此处需要请问
                                print('充值成功!{}的余额为{}'.format(admin1,salary[admin1]))
                            else:
                                print('没有{}这个用户'.format(admin1))
                        else:
                            print('你不是管理员！滚')
                            exit()
                else:
                    if usershop == 'q' or usershop == 'quid':
                        for item in shop_car:
                            print(item)
                            print('欢迎下次光临！！')
                            print('END'.center(40, '*'))
                            print('你的余额为{}'.format(salary[userip1]))
                            exit()
                    elif usershop == 'c' or usershop == 'check':
                        print('已购买的商品'.center(40, '*'))
                        for item in shop_car:
                            print(item)
                        print('END'.center(40, '*'))
                        print('你的余额为{}'.format(salary[userip1]))
        else:
            print('你输入错误！')
            break
    else:
        print('你输入有误，请重新输入')
        break