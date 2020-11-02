"""
======================
Author: 柠檬班-小简
Time: 2020/6/15 21:01
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
datas = [
    {"user":"python27","passwd":"lemonban","check":{"code": 0, "msg": "登录成功"}},
    {"user":"python27","passwd":"lemonban11","check":{"code": 1, "msg": "账号或密码不正确"}},
    {"user":"python25","passwd":"lemonban","check":{"code": 1, "msg": "账号或密码不正确"}}
]

按行读取数据：
    sh.rows = 所有行的数据。list(sh.rows)返回的是一个列表，列表当中的成员：每一个行的数据元组。

"""
import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"login_cases.xlsx")

# 1、加载excel数据文件
from openpyxl import load_workbook
wb = load_workbook(file_path)

# 2、根据表单名称选择表单：wb['表单名称']
sh = wb["login"]

# 1、拿到字典的key值：
# print(list(sh.rows)[0])  # (<Cell 'login'.A1>, <Cell 'login'.B1>, <Cell 'login'.C1>)
titles = []
for item in list(sh.rows)[0]: # 遍历第1行当中每一列
    titles.append(item.value)
print(titles)


data_lists = []
# 2、把key和value组合到一起，形成一个字典。再将字典，放到列表当中。
# # print(list(sh.rows))  # 每一个行是个元组，无组里放的是每一行的单元格。
for item in list(sh.rows)[1:]: # 遍历每一行
    value_dict = {} # 每一行是一个字典。
    print(item)
    for index in range(len(item)):  # 获取每一行的单元格数据
        print(index,item[index],item[index].value)
        value_dict[titles[index]] = item[index].value
    print(value_dict)
    data_lists.append(value_dict) # 将每一行测试数据追加到列表当中。

print(data_lists)


# zip 打包函数

zip()