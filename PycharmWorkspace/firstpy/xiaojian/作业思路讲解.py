"""
======================
Author: 柠檬班-小简
Time: 2020/6/3 19:44
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
一行一行存储
字符串：yuze,17,男,假正经, I am yours
列表当中，每一个字典的values.
list(字典.values())
用逗号将每一个value拼成一个字符串。
"，".join(列表/元组) --- 每一个成员要是字符串
再写入文件当中。

函数 ：封装成函数。
一部分：写文件。
二部分：就是从列表当中，得到一个字符串。
yuze,17,男,假正经, I am yours\n
cainiao,18,女,看书,Lemon is best!
参数：列表
出参：字符串

遍历readlines() - 对每一行进行处理：

    通过@分割
    ["url:/futureloan/mvc/api/member/register","mobile:18866668888","pwd:123456"]
    字典：temp = {}
    遍历每一个成员
    对每一个成员，再根据:切割
    ["url","/futureloan/mvc/api/member/register"] - temp[list[0]] = list[1]
    ["mobile","18866668888"]  - temp[list[0]] = list[1]
    ["pwd","123456"] - temp[list[0]] = list[1]
    
    字典定义在for循环内还是外？
    
    {'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'}

定义一函数：入参：字符串。输出：字典。
"""