# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:35:13 2023

@author: cjj
"""

def getFileText():
    with open("D:\work.0\python\Robin.txt","r")as letterFile:
        fileTxt=letterFile.read()
    fileTxt=fileTxt.lower()
    for ch in'!"#$%&()*+-*/,.:;<=>?@[]\^_{}|~':
        fileTxt=fileTxt.replace(ch, " ")
    return fileTxt
letterTxt=getFileText()
words=letterTxt.split() 
wdCountDict={}
for word in words:
    wdCountDict[word]=wdCountDict.get(word,0)+1

# 根据单词出现次数降序排序
sorted_word_count = sorted(wdCountDict.items(), key=lambda x: x[1], reverse=True)

# 输出频率最高的前10个单词及其个数
print("频率最高的前10个单词及其个数：")
for i in range(min(10, len(sorted_word_count))):
    print(f"{sorted_word_count[i][0]}: {sorted_word_count[i][1]}")    
 
    
 
"""    
valKeyList=[(val,key) for key,val in wdCountDict.items()]
valKeyList.sort(reverse=True)
print("{0:<10}{1:>5}".format("word", "count"))
print("*"*21)
for val,key in valKeyList:
    print("{0:<10}{1:>5}".format(key, val))    
    pass
"""