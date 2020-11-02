"""
======================
Author: 柠檬班-小简
Time: 2020/6/10 21:31
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

# 功能逻辑
def login_check(username=None, password=None):
    """ 登录校验的函数
    :param username: 账号
    :param password: 密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python27' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


"""
1、账号密码正确 
入参：账号python27 密码lemonban 
预期结果：{"code": 0, "msg": "登录成功"} 
实际结果： 

2、账号正确，密码错误 
入参：账号python27 密码lemonban11 
预期结果：{"code": 1, "msg": "账号或密码不正确"} 
实际结果： 

3、账号错误，密码正确， 
入参：账号python25 密码lemonban 
预期结果：{"code": 1, "msg": "账号或密码不正确"} 
实际结果：

4、账号为空 
入参：账号为空 密码lemonban11 
预期结果：{"code": 1, "msg": "所以的参数不能为空"} 
实际结果： 

5、密码为空、 
入参：账号Python6 密码为空 
预期结果：{"code": 1, "msg": "所以的参数不能为空"} 
实际结果 
"""

# s = login_check("python27","lemonban")
# # 比对期望和实际
# if s == {"code": 0, "msg": "登录成功"}:
#     print("用例通过！")
# else:
#     print("用例失败！")
#
#
# s = login_check("python27","lemonban")
# # 比对期望和实际
# if s == {"code": 0, "msg": "登录成功。。"}:
#     print("用例通过！")
# else:
#     print("用例失败！")

# 用例之间是独立的。你失败或者成功，跟另外一个用例的执行+结果都是没有关系的。