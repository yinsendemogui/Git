#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import os,sys
sys.path.append('..')
from lib.Teachers_model import teacher_Model
from lib.Lessons_model import lesson_Model
from lib.Students_model import student_Model



t1 = teacher_Model('陈老师','32','男')
l1 = lesson_Model('生物','6',t1)
t2 = teacher_Model('李老师','32','男')
l2 = lesson_Model('化学','5',t2)
s1 = student_Model('陈思齐','32','1','1',[l1,l2])
s2 = student_Model('田宗浩','26','1','1',[l2])
s1.Classbegins(s1.Lobj[0].Lname)
s1.Classbegins(s1.Lobj[0].Lname)
s1.Classbegins(s1.Lobj[0].Lname)

s2.Classbegins(s2.Lobj[0].Lname)
s2.Classbegins(s2.Lobj[0].Lname)
s2.Classbegins(s2.Lobj[0].Lname)

s1.Classbegins(s1.Lobj[1].Lname)
s1.Classbegins(s1.Lobj[1].Lname)
s1.Classbegins(s1.Lobj[1].Lname)

print (s1.Lobj[0].Tobj.calary_Return())
print (s2.Lobj[0].Tobj.calary_Return())