#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：


class student_Model:
    '''
    学生模型类
    '''
    def __init__(self,name,age,lobj):
        self.Name = name        #姓名
        self.Age = age          #年龄
        self.Lobj = lobj        #课程对象列表


    def Classbegins(self):      #上课
        self.Lobj.classBegins()