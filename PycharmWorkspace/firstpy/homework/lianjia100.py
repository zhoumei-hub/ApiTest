"""
======================
Author: 柠檬班-totoro
Time: 2020/6/21 20:52
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
编写如下程序从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出 提示：

 a. 1!等于 1

 b. 2!等于 1*2

 c. 3!等于 1*2*3



d. n!等于 1*2*3*...*n
"""
num = int(input("请输入一个整数："))

for i in range(1,num+1):
    count = 1
    print("{} ! 等于1".format(i), end=" ")
    for j in range(1,i+1):
        count = count * j
        print("* {}".format(j),end=" " )
    print("")


