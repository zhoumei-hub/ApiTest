"""
======================
Project: firstpy
Time: 2020/9/19 9:34
Author: zhoumei
======================
"""
"""
替换用例中url、request_data、check_sql等有打标的值

"""


class EnvData:
    """
    存储用例要使用到的数据。
    """
    pass



def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case




if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }
    # if case["request_data"].find("#phone#") != -1:
    case = replace_mark_with_data(case, "#phone#", "123456789001")
    for key,value in case.items():
        print(key,value)
