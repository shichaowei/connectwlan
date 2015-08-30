#coding:utf-8
'''
Created on 2015年8月30日
只适用于此前已经连接过的ssid，配置文件没有删除
@author: Administrator
'''
import testnetwork
import ConnectWlan
import time
from web.webapi import rawinput

if __name__ == '__main__':
    while True:
        time.sleep(30)
        temp=testnetwork.testnet("www.baidu.com")
        if temp==0:       
            #此处换成你需要连接的ssid---TP-LINK_2B66
            if ConnectWlan.ConnectWlan("TP-LINK_2B66")==1:
                time.sleep(5)
                tempsec=testnetwork.testnet("www.baidu.com")
                if tempsec==0:
                    print "success to connect wlan,but can't to connect internet"
                else:
                    print "success to connect wlan.We can surf the Internet"
            else:
                print "fail to connect wlan,please confirm the ssid is exist"
        elif temp==1:
            pass
        else:
            print r"未知错误"
        