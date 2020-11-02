"""
======================
Author: 柠檬班-小简
Time: 2020/6/1 21:04
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
# fs = open("py30.txt")
# fs = open(r"D:\Pychram-Workspace\py30\class_2020-0601\py30.txt","a",encoding="utf-8")  # 打开文件

# 读取里面的数据
# 饮用水 -
# s = fs.read() # 字符串
# print(s)
# s1 = fs.readline()
# print(s1)
# s2 = fs.readline()
# print(s2)
# s = fs.readlines()
# print(s)

# 使用了外部的资源 ，在使用之后都要关闭。
# fs.write("大家好，hello,World！111111\n") # w模式  文件覆盖写入
# fs.write("py30,year!!!!")
# fs.close()  # 关闭文件，释放资料。 第三方资源。

# 追加。在原有的文件内容之后，追加新的内容。
# 打开文件的时候，模式为a -append
# fs.write("\n追加者号！！！")
# fs.close()

# 写、追加  如果文件不存在，自动创建 。
# 如果文件所在的目录不存在，则会报错。
# fs = open("new_file.txt","a",encoding="utf-8")
# # fs = open(r"D:\Pychram-Workspace\class_2020-0601\new_file.txt") # FileNotFoundError: [Errno 2] No such file or directory
# fs.write("我是新的文件！hello,python!")
# fs.close()

# 会主动关闭文件的。不需要你调用close()
with open("new_file.txt","a",encoding="utf-8") as fs:
    fs.write("我是新的文件！hello,python!")



# 可读可写  +  rw(不行)
# r+ 可读可追加
# w+ 先清除内容
# fs = open("new_file.txt",encoding="utf-8",mode="w+")
# print(fs.read())
# fs.write("ssssss")
# fs.close()

# 打开第三方资源的时候，用完了就关闭资源。释放出来。close()








