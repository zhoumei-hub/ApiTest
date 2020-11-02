
"""
文件操作练习题
name:totoro
"""


"""
1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表），格式如下：
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]
创建一个txt文本文件，来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto
b.从第二行开始，每行添加具体用户信息，例如：
yuze,17,男,假正经, I am yours
cainiao,18,女,看书,Lemon is best!

"""
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"},{"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}]
# 将age的值转换成字符串，便于拼接
person_info[0]["age"] = str(person_info[0]["age"])
person_info[1]["age"] = str(person_info[0]["age"])

# 取字典的值转换成列表，然后拼接成字符串
aa1 =list(person_info[0].values())
ss1 = ",".join(aa1)
aa2 =list(person_info[1].values())
ss2 = ",".join(aa2)

with open("new_file.txt","a",encoding="utf-8") as fs:
    fs.write("name,age,gender,hobby,motto\n")
    fs.write(ss1)
    fs.write("\n")
    fs.write(ss2)










"""
编写如下程序
有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：

url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456

url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）

[{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
"""

with open("my_file.txt","w",encoding="utf-8") as fs:
    fs.write("url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\n")
    fs.write("url:/futureloan/mvc/api/member/recharge@mobile:18866668889@amount:1000")


def my_data():
    with open("my_file.txt", "r", encoding="utf-8") as fs:
        list_a = fs.readlines()
    list_b = []
    for i in range(len(list_a)):#循环2次
        list1 = (list_a[i].replace("\n","")).split("@") #将换行符替换掉，再根据@切片成列表
        list3 = []
        for j in range(len(list1)):#循环3次
            list3.append(list1[j].split(":")) #list1中每个元素根据：切片，切片后append到list3
        list_b.append(dict(list3)) #使用dict函数将列表中的列表转换成字典append到list_b中
    print(list_b)
    return  list_b

my_data()