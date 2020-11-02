"""
======================
Author: 柠檬班-小简
Time: 2020/8/12 20:55
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
selenium - 工具包

ide: 录制工具。
webdriver: 第三方库。结合代码来使用。python,java,c#...
grid: 分布式。

安装第三方库：
pip install -U selenium

web自动化环境：
  人 --- 浏览器 - 打开页面，点点点
代码 --- 浏览器 - 打开页面，点点点

代码       <--->    中间物种(浏览器驱动程序)    <--->  浏览器(ie、firefox、google)
指令(客户端)         执行指令(地址+端口 - 服务端)
打开一个浏览器        每个浏览器都有一个驱动程序       
访问百度首页           ieserverDriver
输入用户名             geckodriver
输入密码               chromedriver
点击搜索            驱动程序要跟浏览器版本匹配
selenium        http://npm.taobao.org/mirrors/chromedriver/

驱动地址：
Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads  .       
国内镜像地址：http://npm.taobao.org/mirrors/chromedriver/

Edge:  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:  https://github.com/mozilla/geckodriver/releases
Safari:  https://webkit.org/blog/6900/webdriver-support-in-safari-10/

selenium+python环境安装博客地址：
https://www.cnblogs.com/Simple-Small/p/10065674.html
"""
