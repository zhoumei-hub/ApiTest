""""
柠檬班-Python30期
totoro
"""

"""
1、现在有字符串：str1 = 'python cainiao 666'

    1、请找出第 5 个字符。  

    2、请复制一份字符串，保存为 str_two(使用赋值哦)

    3、请找出最中间的字符。（字符串长度是偶数。）
"""

str1 = 'python cainiao 666'
# 1、请找出第 5 个字符。
print(str1[4])
# 2、请复制一份字符串，保存为 str_two(使用赋值哦)
str_two = str1
print(str_two)
# 3、请找出最中间的字符。（字符串长度是偶数。）
index1 = len(str1) // 2
index2 = (len(str1) // 2) -1
str3 = str1[index1]
str4 = str1[index2]
#最中间2个字符
print(str3)
print(str4)

"""
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）

      (使用input方法获取用户输入哦)
"""
price = input("请输入橘子的价格：")
weight = input("请输入橘子的重量：")
total_price = int(price) * int(weight)
print(total_price)

"""
3.演练字符串操作
my_hobby = "Never stop learning!"

截取从 位置2 ~ 位置6 的字符串

截取从 位置2 ~ 末尾 的字符串

截取从 开始位置~ 位置6 的字符串

截取完整的字符串

从 索引3 开始，每2个字符中取一个字符

截取字符串末尾两个字符

字符串的倒序

说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
"""
my_hobby = "Never stop learning!"
# # 截取从 位置2 ~ 位置6 的字符串
print(my_hobby[1:6])
# # 截取从 位置2 ~ 末尾 的字符串
print(my_hobby[1:])
# # 截取从 开始位置~ 位置6 的字符串
print(my_hobby[0:6])
# # 截取完整的字符串
print(my_hobby[:])
# # 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])
# # 截取字符串末尾两个字符
print(my_hobby[-1:-3:-1])
# # 字符串的倒序
print(my_hobby[::-1])

"""
4， 总结本节课内容，画出思维导图或者笔记详情

<20200520学习笔记>
python运算符：
算数运算： + - * / %
赋值运算：赋值给变量   =（赋值）       += （累加）       -=（累减）
比较运算：==（等于）  ！=    >   >=      <     <=   比较结果为布尔值，True Flase
逻辑运算：and     or    not   比较结果为布尔值，True Flase


字符串的定义：
单引号、双引号、三引号，外面是单引号，里面用双引号；外面是双引号，里面用单引号，注意区分
空字符串 s = ''
转换成字符串 str()

字符串索引：
正向：从0开始      反向：从-1开始

字符串切片：
格式： 字符串[起始索引:结束索引:步长]  my_hobby[1:6：2]
起始索引默认0，步长默认1
左开右闭，步长为正，正切；步长为负，倒序切，字符串反转[:：-1]

字符串操作方法：
find（找到元素的位置）
count(找到元素个数)
len(获取字符串长度)
upper(将字符串字母转换成大写)

"""
