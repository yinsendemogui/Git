#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tian
import time
TAG = True
PROVINCE = {'1':'河北','2':'山西','3':'陕西'}
LIST = ['1','2','3','4']
MUTUAL = {'1':{'1':['石家庄','赞皇金丝大枣,藁城宫面'],'2':['承德','烧卖、油酥饽饽、八宝饭、二仙居碗坨'],
            '3':['衡水','老白干，衡水湖，贾岛'],'4':['邯郸','豫剧桑派艺术、鸡泽梨花大鼓、永年武式太极拳']},
          '2':{'1':['太原','晋祠、天龙山石窟、永祚寺、崇善寺'],'2':['运城','解州关帝庙、永乐宫、鹳雀楼、运城盐湖'],
             '3':['大同','云冈石窟、恒山、善化寺、华严寺'],'4':['临汾','华门、尧庙、壶口瀑布、洪洞大槐树']},
          '3':{'1':['西安','兵马俑、钟鼓楼、大雁塔、小雁塔'],'2':['汉中','西汉三遗址、褒斜栈道、武侯墓'],
             '3':['宝鸡','法门寺、太白山；关山草原、红河谷'],'4':['韩城','韩城古城、司马迁祠墓、大禹庙']}}

print ('      Welcome China!')
while TAG:
    print ('''    1--------河北
    2--------山西
    3--------陕西
    ''')
    choice = raw_input('您关注哪个省份或退出q？:')
    if choice in '123':
        while TAG:
            for i in LIST:
                print i, '--------', MUTUAL[choice][i][0]
            choice_1 = raw_input('您想了解哪个城市或b返回上一层/q退出？:')
            if choice_1 in '1234':
                print ('您的选择是{},地方特色有:{}').format(MUTUAL[choice][choice_1][0],MUTUAL[choice][choice_1][1])
                qb = raw_input('b返回上层/q退出/c继续: ')
                if qb == 'b': continue
                elif qb == 'q': exit()
                elif qb == 'c': break
                else: time.sleep(5);print('无此项，请重输')
            elif choice_1 == 'q':
                print ('Say Goodbye!')
                exit()
            elif choice_1 == 'b':
                break
            else: print('您输入超标')
    elif choice == 'q':
        print ('欢迎下次再来')
        exit()
    else:
        print ('您的选择有误！')