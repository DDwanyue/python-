# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:47:12 2023

@author: cjj
"""

print("|---欢迎进入通讯录程序---|")
print("|---1:查询全部联系人---|")
print("|---2:查询特定联系人---|")
print("|---3:更新联系人信息---|")
print("|---4:插入新的联系人---|")
print("|---5:删除已有联系人---|")
print("|---6:清除全部联系人---|")
print("|---7:退出通讯录程序---|")
print("")
#构建字典，存储联系人信息
dict={'zhangsan':'13813593298','lisi':'13586366317','wangwu':'13813762582'}
#列表元素
d2=[{'name':'zhangsan','age':20,'tel'}]
#定义各功能函数
#查询所有联系人信息
def queryAll():
    if dict=={}:
        print('通讯录无如何联系人信息')
    else:
        i=1
        for key,value in dict.items():
            print("{0}姓名：{1},电话号码：{2}".format(i, key,value))
            i=i+1
#查询一个联系人的信息
def queryOne():
    name=input('请输入要查询的联系人姓名：')
    print(name + ":"+dict.get(name,'联系人不存在'))
    pass
def update():
    name=input("请输入要修改的联系人姓名：")
    if(name in dict):
        value=input("请输入电话号码：")
        dict[name]=value
    else:
        print("联系人不存在")
#插入一个新联系人
def insertOne():
    name=input("请输入要插入的联系人姓名：")
    if(name in dict):
        print("您输入的姓名在通讯录中已存在"+"-->>"+ name +":"+dict[name])
        iis=input("输入'Y'修改用户资料，输入其他字符结束插入联系人")
        if iis in['YES','yes','Y','y','Yes']:
            value=input("请输入电话号码：")
            dict[name]=value
    else:
        value=input("请输入电话号码：")
        dict[name]=value
#删除一个联系人
def deleteOne():
    name=input("请输入联系人姓名：")
    value=dict.pop(name,'联系人不存在')
    if value=='联系人不存在':
        print("联系人不存在")
    else:
        print("联系人"+name+"已删除")
    pass
#清空通讯录
def clearAll():
    cis=input("提示：确认清空通讯录吗？确认操作输入'Y',输入其他字符退出")
    if cis in['YES','yes','Y','y','Yes']:
        dict.clear()
    pass
            
#构建无限循环，实现重复操作
while True:
    n=input("请根据菜单输入操作序号：")
    if(n=='1'):
        queryAll()
    elif(n=='2'):
        queryOne()
    elif(n=='3'):
        update()
    elif(n=='4'):
        insertOne()
    elif(n=='5'):
        deleteOne()
    elif(n=='6'):
        clearAll()
    elif(n=='7'):
        print("|---感谢使用通讯录程序---|")
        print("")
        break   #结束循环，退出程序
        
            