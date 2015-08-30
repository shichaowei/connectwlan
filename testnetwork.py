#coding:utf-8


import re 
import sys,os
import commands
import datetime
import time
'''
Created on 2015年8月30日

@author: Administrator
'''

def deletefile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print filename+'is not exist'
    
    
    
    
def testnetfile(filename):
    file=open(filename,'r')
    for i in file.readlines():
        #找不到返回-1，找到返回相应的索引值
        if i.find("TTL=") != -1:
            return 1
            break
    return 0

        


def testnet(ip):
    if os.path.exists('file.txt'):
        os.remove('file.txt')
    else:
        pass    
    cmd='ping -n 1 %s>>file.txt' % (ip.strip())
    os.system(cmd)   #windows only
    if testnetfile('file.txt')==0:
        print "net is fail"
        return 0
    else:
        print "net is OK"
        return 1
    deletefile('file.txt')
         
    

    
    
    
if __name__ == '__main__':
    testnet('www.baidu.com')


        
           