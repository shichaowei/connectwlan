#coding:utf-8
'''
Created on 2015��6��10��

@author: wkf5506
'''

def store(string):
    file=open('test.txt','a')
    file.write(string)    
    file.write('\n')
    file.close()


