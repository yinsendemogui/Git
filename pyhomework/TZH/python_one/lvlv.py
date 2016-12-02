#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import time
FU = True
TAG = True
PROVINCE = {'1':'河北','2':'山西','3':'陕西'}
LIST = ['1','2','3','4']
MUTUAL = {'1':{'1':['石家庄','赞皇金丝大枣,藁城宫面'],'2':['承德','烧卖、油酥饽饽、八宝饭、二仙居碗坨'],
            '3':['衡水','老白干，衡水湖，贾岛'],'4':['邯郸','豫剧桑派艺术、鸡泽梨花大鼓、永年武式太极拳']},
          '2':{'1':['太原','晋祠、天龙山石窟、永祚寺、崇善寺'],'2':['运城','解州关帝庙、永乐宫、鹳雀楼、运城盐湖'],
             '3':['大同','云冈石窟、恒山、善化寺、华严寺'],'4':['临汾','华门、尧庙、壶口瀑布、洪洞大槐树']},
          '3':{'1':['西安','兵马俑、钟鼓楼、大雁塔、小雁塔'],'2':['汉中','西汉三遗址、褒斜栈道、武侯墓'],
             '3':['宝鸡','法门寺、太白山；关山草原、红河谷'],'4':['韩城','韩城古城、司马迁祠墓、大禹庙']}}

while TAG:
    if FU == True:
        print ('''        1--------河北
        2--------山西
        3--------陕西
        ''')
        choice = raw_input('Pls input province index or q/b:')
        if choice in '123':
            for i in LIST:
                print i, '--------', MUTUAL[choice][i][0]
            choice_1 = raw_input('which city you choice or q/b:')
            if choice_1 in '1234':
                print ('You choice {},The feature is: {}').format(MUTUAL[choice][choice_1][0],MUTUAL[choice][choice_1][1])
                time.sleep(5);exit()
            elif choice_1 == 'q':
                exit()
            elif choice_1 == 'b':
                continue
            else: FU = False;print ('try again')
        elif choice == 'q':
            print ('byebye!')
            exit()
        elif choice == 'b':
            print 'sory'
        else:
            print ('Try again')
    else:
        if choice in '123':
            for i in LIST:
                print i, '--------', MUTUAL[choice][i][0]
            choice_1 = raw_input('which city you choice or q/b:')
            if choice_1 in '1234':
                print ('You choice {},The feature is: {}').format(MUTUAL[choice][choice_1][0],MUTUAL[choice][choice_1][1])
                time.sleep(5);exit()
            elif choice_1 == 'q':
                exit()
            elif choice_1 == 'b':
                continue
            else: FU == False;break
        elif choice == 'q':
            print ('byebye!')
            exit()
        elif choice == 'b':
            print 'sory'
        else:
            print ('Try again')
        FU = True