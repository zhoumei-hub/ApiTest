
"""
1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
"""
original_price = input("请输入购买商品的价格：")

if  50 <= int(original_price) <= 100:
    print("您享受的折扣是10%！")
    pay = int(original_price) - int(original_price)*0.1
elif int(original_price) > 100:
    print("您享受的折扣是20%！")
    pay = int(original_price) - int(original_price)*0.2
else:
    print("您没有任何折扣！")
    pay = int(original_price)
print("您需要支付的金额为{}元".format(pay))


"""
2 判断是否为闰年
提示:
输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
什么是闰年，请自行了解（需求文档没有解释）
"""
r_year = input("请输入年份：")
aa = int(r_year) % 4
if aa == 0:
    print("{}年是闰年".format(r_year))
else:
    print("{}年不是闰年".format(r_year))



"""
3.求三个整数中的最大值
提示：定义 3 个变量
"""
num1 = input("请输入第一个整数：")
num2 = input("请输入第二个整数：")
num3 = input("请输入第三个整数：")

if int(num1) >= int(num2):
    aa = int(num1)
else:
    aa = int(num2)
if aa >= int(num3):
    max = aa
else:
    max = int(num3)
print("{}，{}，{}中最大整数为{}".format(num1,num2,num3,max))


"""
4，  使用for打印九九乘法表

提示：

输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1	
1 * 2 = 2    2 * 2 = 4	
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9	
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16	
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25	
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36	
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49	
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64	
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
"""

for i in range(1,10):
    for j in range(1,i+1):
        value1 = i * j
        print("{} * {} = {}".format(j,i,value1),end="\t")
    print("")

