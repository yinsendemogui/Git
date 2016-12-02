#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：



class lesson_Model:
    '''
    课程模型类
    '''
    def __init__(self,lname,lcost,tobj):
        self.Lname = lname      #课程名
        self.Lcost = lcost      #课时费
        self.Tobj = tobj        #老师对象

    def classBegins(self):      #上课方法
        if lesson_Model.success_Radio():
            self.Tobj.Calary += 5
        else:
            self.Tobj.teacher_Accident()


    def success_Radio():
        return True
