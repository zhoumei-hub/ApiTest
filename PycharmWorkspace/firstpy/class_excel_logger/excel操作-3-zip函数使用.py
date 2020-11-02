"""
======================
Author: 柠檬班-小简
Time: 2020/6/15 21:34
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""

zip函数

eval函数(字符串) 转成python语句执行
"""
# li1 = ['user', 'passwd', 'check']
# li2 = ["python27","lemonban66666",{"code": 0, "msg": "登录成功"}]
#
# res = zip(li1,li2)
# print(dict(res))

import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"login_cases.xlsx")

# 1、加载excel数据文件
from openpyxl import load_workbook
wb = load_workbook(file_path)

# 2、根据表单名称选择表单：wb['表单名称']
sh = wb["login"]

all_datas = []  # 获取excel表格当中所有的测试数据
# 1、拿到字典的key值：
# print(list(sh.rows)[0])  # (<Cell 'login'.A1>, <Cell 'login'.B1>, <Cell 'login'.C1>)
titles = []
for item in list(sh.rows)[0]: # 遍历第1行当中每一列
    titles.append(item.value)
print(titles)

for item in list(sh.rows)[1:]: # 遍历数据行
    values = []
    for val in item:  # 获取每一行的值
        values.append(val.value)
    res = dict(zip(titles,values))  # title和每一行数据，打包成字典
    res["check"] = eval(res["check"])  # 将check的字符串，转换为字典对象。
    all_datas.append(res) # 追加到列表

print(all_datas)