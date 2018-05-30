
推送服务
PC端 - websocket / SockJS / STOMP
移动端 - 第三方平台(极光/百度/小米/友盟)


### linux 配置 mongodb
>>> 1. https://www.mongodb.com/download-center#atlas
2. wget<url>
3. gunzip <filename>
4. tar -xvf <filename>
5. mv <source> /usr/local/<source>
6. vim .bash_profile PATH=.....  :/usr/local/<source>/bin/
如果没有这个文件，则 PATH=$PATH:/usr/local/mongo-3.6.5/bin/
7. source .bash_profile
8. echo $PATH
8. mkdir -p /data/db
9. mongodb
10. 配置防火墙

fg %1把程序放到前台运行
mongod --bind_ip ifconfig查到的ip地址 --quiet &
(自己连接就需要输入mongo --host 私网ip)


输入mongo进入交互式环境后输入db，出现test就表示成功

mongo图形界面连接不上mongodb的情况下：1.考虑防火墙， 2.是否启动服务