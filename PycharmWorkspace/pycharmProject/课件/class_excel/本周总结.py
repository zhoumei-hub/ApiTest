"""
======================
Author: 柠檬班-小简
Time: 2020/6/15 21:53
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、excel操作：openpyxl模板
   WorkBook
   Sheet
   Cell

  测试数据文件，提前准备好。
  wb = load_workbook(file_path)
  # 表单
  sh = wb["表单名称“]
  # 获取表单当中所有的数据 - 按行获取
  sh.rows =》 list(sh.rows) == 列表的成员是元组。
  每一行是个元组，元组里的成员是cell对象。
  
  all_cases = []  # 存放读取出来的所有测试数据
  
  # 遍历行，获取每一行当中，所有列的数据。
    每一行数据，存储在字典当中。一行代码一个测试用例数据。
      key:value
      key: 遍历第一行，
      titles = []
      for cel in list(sh.rows)[0]:
            titles.append(cel.value)
    
    从第二行开始，每一行是一个测试用例数据。
    先遍历行，在行当中，再遍历列。
    for row in list(sh.rows)[1:]:
        values = []
        for cel in row:
            values.append(cel.value)
        case_data = dict(zip(titles,values))
        # 有一个key的值，要求是字典
        case_data["check"] = eval(case_data["check"])
        all_cases.apend(case_data)
                        
    将每一行的字典，添加到列表当中。

"""