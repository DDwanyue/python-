# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 07:57:37 2023

@author: cjj
"""

#letter.py
def getFileText():
    with open("D:\work.0\python\letter.txt","r")as letterFile:
        fileTxt=letterFile.read()
    fileTxt=fileTxt.lower()
    for ch in'!"#$%&()*+-*/,.:;<=>?@[]\^_{}|~':
        fileTxt=fileTxt.replace(ch, " ")
    return fileTxt
letterTxt=getFileText()
words=letterTxt.split()

        
    pass