"""
======================
Author: 柠檬班-小简
Time: 2020/8/12 20:39
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
8种定位方式 - html页面

定位：在整个html当中，根据元素的特色，找到它！

根据元素的一个特征来定位。6种。

id: 元素的id属性。- 唯一。

class: 元素的class属性
tag: 元素的标签名
name: 元素的name属性
针对a元素：
link_text: 针对a元素的文本内容 - 完全匹配
partial_link_text: 针对a元素的文本内容 - 包含


组合元素的多种特征/关系 ，来定位。2种 - 万能定位。
xpath：
css selector: css选择器

定位的时候：
1、确认你要找的元素是谁
2、通过F12查看你的元素特征
"""
from time import sleep

# 引入第三方库
from selenium import webdriver
# 打开浏览器 - 指令1 - 开启与浏览器之间的会话。
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 访问百度首页 - 指令2
driver.get("http://www.baidu.com")
# 通过定位表达式，找到对应的元素
# element = driver.find_element_by_id("kw")  # WebElement对象
# print(element)
# print(element.tag_name)
# # 在找到的元素中，输入文本
# element.send_keys("selenium webdriver")

# 合并写法
driver.find_element_by_id("kw").send_keys("selenium webdriver")


sleep(7)
# 关闭当前窗口。
driver.close()
# 关闭浏览器，关闭会话。
driver.quit()


