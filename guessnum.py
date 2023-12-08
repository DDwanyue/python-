# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:21:13 2023

@author: cjj
"""
#猜数字游戏
import random
num=random.randrange(0,100)
time=0
#开始游戏
print(
'''
      欢迎参加猜数字游戏
      猜一个100以内的数字
'''
      )
guess=int(input("\n请输入数字"))
while guess!=num and guess!="":
    if guess<num:
        print("你猜的数字偏小！")
        guess=int(input("\n继续猜"))
        time+=1
    else:
        print("你猜的数字偏大！")
        guess=int(input("\n继续猜"))
        time+=1
if guess==num:
    time+=1
    print("恭喜!你猜对了，共猜了%d次" %(time))
