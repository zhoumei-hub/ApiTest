"""
======================
Author: 柠檬班-totoro
Time: 2020/5/25 20:19
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""
num_list = [1,2,5,3,4]
# 升序
num_list.sort()
print(num_list)
# 降序
num_list.sort(reverse=True)
print(num_list)
# 反转
print(num_list[::-1])
num_list.reverse()

# () 括号 tuple 不放列表和字典这种可变的
my_tuple = ()
my_tuple2 = (18,45,32)
print(my_tuple2[1])


# dict 字典
dog_info = {
    "name" : "欢欢",
    "sex" : "公",
    "type" : "串串"
}

print(dog_info)
print(dog_info["name"])
print(dog_info.get("name"))
dog_other_info = {"color":"白色","size":"40cm"}
dog_info.update(dog_other_info)
print(dog_info)
dog_info["other_info"] =  {"color":"白色","size":"40cm"}
print(dog_info)

# 控制流 if 判断 顺序执行
score = input("请输入你的成绩：")
if 85 <= int(score)<= 100 :
    print("A")
    print("perfect!")
elif 75 <= int(score)< 85:
    print("B")
else:
    print("不及格")
print("no")