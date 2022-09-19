#### 该程序实现Linux操作系统锐捷校园网环境下，断网自动重连。

其原理为使用python中的OS模块不断调用锐捷客户端程序实现登录，若ping不通谷歌的DNS服务器，则根据返回值来调用程序进行连接。

该程序为x86架构,无法在诸如树莓派的arm架构下运行

usage：

1.首先在shell中键入ifconfig找到自己的网卡设备名，如eth0,在demo.py中-n 标签后进行替换

2.然后在将your_account和your_passwd替换为自己的校园网账号和密码

3.最后在shell中键入python demo.py即可开始运行程序

tips：注意程序的权限问题，权限不足可能出现异常
