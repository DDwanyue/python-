# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:41:05 2023

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
#列表元素
# 构建列表，存储联系人信息
contacts = [
    {'name': 'zhangsan', 'age': 20, 'tel': '13813593298'},
    {'name': 'lisi', 'age': 22, 'tel': '13586366317'},
    {'name': 'wangwu', 'age': 19, 'tel': '13813762582'}
]

# 定义各功能函数
# 查询所有联系人信息
def queryAll():
    if not contacts:
        print('通讯录无如何联系人信息')
    else:
        for i, contact in enumerate(contacts, 1):
            print("{0}姓名：{1}, 年龄：{2}, 电话号码：{3}".format(i, contact['name'], \
                                                       contact['age'], contact['tel']))
# 查询一个联系人的信息
def queryOne():
    name = input('请输入要查询的联系人姓名：')
    for contact in contacts:
        if contact['name'] == name:
            print("姓名：{0}，年龄：{1}，电话号码：{2}".format(contact['name'], \
                                                  contact['age'], contact['tel']))
            return
    print('联系人不存在')
# 更新联系人信息
def update():
    name = input("请输入要修改的联系人姓名：")
    for contact in contacts:
        if contact['name'] == name:
            value_age = int(input("请输入新的年龄："))
            value_tel = input("请输入新的电话号码：")
            contact['tel'] = value_tel
            contact['age'] = value_age
            print("联系人信息已更新")
            return
    print("联系人不存在")
# 插入一个新联系人
def insertOne():
    name = input("请输入要插入的联系人姓名：")
    for contact in contacts:
        if contact['name'] == name:
            print("您输入的姓名在通讯录中已存在" + "-->>" + "{0}：{1}，年龄：{2}，\
                  电话号码：{3}".format(name, contact['age'], contact['tel']))
            iis = input("输入'Y'修改用户资料，输入其他字符结束插入联系人")
            if iis in ['YES', 'yes', 'Y', 'y', 'Yes']:
                value = input("请输入电话号码：")
                contact['tel'] = value
            return
    age = int(input("请输入年龄："))
    value = input("请输入电话号码：")
    contacts.append({'name': name, 'age': age, 'tel': value})
# 删除一个联系人
def deleteOne():
    name = input("请输入联系人姓名：")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("联系人{0}已删除".format(name))
            return
    print("联系人不存在")
# 清空通讯录
def clearAll():
    cis = input("提示：确认清空通讯录吗？确认操作输入'Y',输入其他字符退出")
    if cis in ['YES', 'yes', 'Y', 'y', 'Yes']:
        contacts.clear()

# 构建无限循环，实现重复操作
while True:
    n = input("请根据菜单输入操作序号：")
    if n == '1':
        queryAll()
    elif n == '2':
        queryOne()
    elif n == '3':
        update()
    elif n == '4':
        insertOne()
    elif n == '5':
        deleteOne()
    elif n == '6':
        clearAll()
    elif n == '7':
        print("|---感谢使用通讯录程序---|")
        print("")
        break  # 结束循环，退出程序。
