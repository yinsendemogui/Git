#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import os
import time
import hashlib
import random
import shop_wel
import shopping
import shop_car
import accounts
import history
import online

TAG = True
# 当前目录
PRESENT = os.getcwd()
# 上层目录
UPPER = os.path.abspath(os.path.join(os.path.dirname('shop_run.py'), os.path.pardir))

# 生成或切换至配置文件目录
def judge():
    os.chdir(UPPER)
    if not os.path.exists('shop_conf'):
        os.mkdir(os.path.join(UPPER,'shop_conf'))
    os.chdir(os.path.join(UPPER,'shop_conf'))

# 切换至代码目录
def code():
    os.chdir(PRESENT)

# 退出函数
def out_quit():
    print ('正在退出商城，请稍后。。。。。')
    time.sleep(2)
    print ('******欢迎下次光临******')
    exit()

FUN_DICT = {'1':shopping.trade,'2':shop_car.cart,'3':accounts.settle,
            '4':history.past,'5':online.bank,'6':out_quit}


# 运行开始
def run():
    while TAG:
        user = raw_input('请输入您的登录用户名：')
        pwd = hashlib.md5(raw_input('请输入您的密码：')).hexdigest()
        # while TAG:                                                      # 验证码
        #     li_code = []
        #     for i in xrange(6):
        #         r = random.randrange(1,7)
        #         if r == 1 or r == 6:
        #             a = random.randrange(10)
        #             li_code.append(str(a))
        #         elif r == 2 or r == 5:
        #             b = random.randrange(65,91)
        #             li_code.append(chr(b))
        #         else:
        #             c = random.randrange(97,123)
        #             li_code.append(chr(c))
        #         yzm = ''.join(li_code)
        #     yan = raw_input('请输入验证码({}):'.format(yzm))
        #     if yan == yzm:
        #         break
        #     else:
        #         print ('验证码输入有误，请重新输入')
        judge()
        if os.path.exists('user.conf'):                           # 有用户配置文件
            judge()
            f = open('user.conf', 'r')
            for line in f:
                local = line.split('|')
                if len(local) == 3:
                    user_local = line.split('|')[0]
                    pwd_local = line.split('|')[1]
                    salary = line.split('|')[2].strip()
                else:
                    continue
            if user == user_local and pwd == pwd_local:
                break
            else:
                print ('您输入的用户名或密码错误，请重新输入')
            code()
        else:
            while TAG:
                input_choice = raw_input('欢迎光临{},您首次登陆ABC购物商城，是否进行充值(y/n):'.format(user))
                if input_choice[0].strip().lower() == 'y':                  # 进行充值
                    while TAG:
                        salary = raw_input('请输入您要充值的金额：')
                        if salary.isdigit():
                            f = open('user.conf', 'w')
                            f.write('|'.join([user, pwd, salary])+'\n')
                            f.write('\n'+'[购物车商品]'+'\n')
                            f.write('\n'+'\n'+'[历史信息]'+'\n')
                            f.close()
                            break
                        else:
                            print ('您输入的金额有误，请重新输入')
                    break
                elif input_choice[0].strip().lower() == 'n':                # 放弃充值
                    salary = str(0)
                    f = open('user.conf', 'w')
                    f.write('|'.join([user,pwd, salary])+'\n')
                    f.write('\n' + '[购物车商品]' + '\n')
                    f.write('\n' + '\n' + '[历史信息]' + '\n')
                    f.close()
                    break
                else:
                    print ('您的选择有误，请重新输入')
            break
            code()

    print ('亲爱的{},欢迎光临ABC购物商城，您的账户余额为{}元'.format(user,salary).center(120,'*')+'\n')
    while TAG:
        shop_wel.welcome()
        function_choice = raw_input('请输入您需要的功能: ')
        for key in FUN_DICT:
            if key == function_choice:
                FUN_DICT[function_choice]()
    else:
        print ('您输入的有误，请选择(1/2/3/4/5/6)')
        # if function_choice == '1':
        #     shopping.trade()
        # elif function_choice == '2':
        #     shop_car.cart()
        # elif function_choice == '3':
        #     accounts.settle()
        # elif function_choice == '4':
        #     history.past()
        # elif function_choice == '5':
        #     online.bank()
        # elif function_choice == '6':
        #     print ('正在退出商城，请稍后。。。。。')
        #     time.sleep(2)
        #     print ('******欢迎下次光临******')
        #     exit()
        # else:
        #     print ('您输入的有误，请选择(1/2/3/4/5/6)')