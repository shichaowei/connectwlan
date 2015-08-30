# connectwlan
在实际工作中，我们会遇到网卡无缘无故掉线，重新连接又可以上线；主要完成测试网络和连接无线的功能，用于windows环境下
1.main函数在autoconnectwlan.py，修改ssid为你需要连接的ssid
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
2.py2exe.py可以在没有安装python的window机子上运行，执行python setup.py py2exe 即可生成exe
setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.5.0",
    description = "py2exe sample script",
    name = "py2exe samples",

    # targets to build
    #windows = ["test_wx.py"],
    console = ["autoconnectwlan.py"],   #修改为你自己的模块名称
    )
