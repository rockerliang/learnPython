#!/usr/bin/env python
 #-*- coding: utf-8 -*-
 #My first python learn

 #python 迭代
d = {'a':1,'b':2,'c':3}
for key in d:
 	print(key)

for value in d.values():
 	print(value)

for  i,value in enumerate(d):
 	print(i,value)

#列表生成式
a = list(range(1,11))
print a

b = [x*x for x in range(1,11)]
print b

L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print L1,L2

