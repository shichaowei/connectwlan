#coding:utf-8
'''
Created on 2015��8��30��

@author: Administrator
'''
import re 
import sys,os
import commands

def ConnectWlan(ssid):
    cmd='netsh wlan connect %s' %ssid
    if os.system(cmd)==0:
        print "wlan connect ok"
        return 1
    else:
        return 0
   
if __name__=="__main__":
    ConnectWlan("TP-LINK_2B66")
   
    