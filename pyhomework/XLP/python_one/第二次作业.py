#!/usr/bin/env python
# _*_ conding:utf-8 _*_
# author: dengliping
dic1 = {'1':'亚洲','2':'非洲','3':'美洲'}
dic2 = {'1':["北京","四川","山东"],'2':["南非","北非","中非"],'3':["美国","巴西","辣眼睛"]}
dic3 = {'1':['丰台区','朝阳区','西城区'],'2':['南充','广安','乐山'],'3':['青岛','青海','嘿嘿']}
dic4 = {'1':['刚果','苏丹','北苏丹'],'2':['沙漠','呵呵','龙卷风'],'3':['哈哈','日本','张三丰']}
dic5 = {'1':['华盛顿','纽约','旧金山'],'2':['南巴西','中巴西','北巴西'],'3':['我曹','握草','我曹']}
FLAG = True
while FLAG:
    print('一级目录{}'.format(dic1))
    dir1_chioce = input('输入123，选择相应大洲，q或b直接退出程序:   ')
    if dir1_chioce == 'q' or dir1_chioce == 'b':
        print('程序结束')
        exit()
    elif dir1_chioce in['1','2','3']:
        print('二级目录{},{},{}'.format(dic2[dir1_chioce][0], dic2[dir1_chioce][1], dic2[dir1_chioce][2]))
        while FLAG:
            dir2_chioce = input('输入123，选择相应省份，q直接退出程序，b返回上级目录:   ')
            if dir2_chioce == 'q':
                print('退出程序')
                exit()
            elif dir2_chioce == 'b':
                break
            elif dir2_chioce in dic3 :
                print('三级目录{},{},{}'.format(dic3[dir2_chioce][0],dic3[dir2_chioce][1],dic3[dir2_chioce][2]))
                break
            elif dir2_chioce in dic4:
                print('三级目录{},{},{}'.format(dic4[dir2_chioce][0],dic4[dir2_chioce][1],dic4[dir2_chioce][2]))
                break
            elif dir2_chioce in dic5:
                print('三级目录{},{},{}'.format(dic5[dir2_chioce][0],dic5[dir2_chioce][1],dic5[dir2_chioce][2]))
                break
    else:
        print('输入错误，请重新输入')