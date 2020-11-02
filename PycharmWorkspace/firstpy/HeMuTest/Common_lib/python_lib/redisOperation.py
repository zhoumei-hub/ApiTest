#! /usr/bin/env python3
# -*- coding utf-8 -*-

import redis
from logHander import log_print


class RedisOperation:

    def __init__(self,host,port,password):
        self.host = host
        self.port = port
        self.password = password

    def get_redis_value(self,key):
        """
        根据键值key查询redis数据
        :param key: 入参传入redis的key键值
        :return: 返回查询到的数据
        """
        self.key = key
        try:
            r = redis.Redis(host = self.host, port = self.port, db = 0, password = self.password)
        except Exception as e:
            log_print('Something wrong when connect the redis ...',e)
        if r.exists(self.key):
            get_res = r.get(self.key).decode('utf8')
        else:
            log_print('the redis_key is not exist')
            get_res = 'Not exist'
        return get_res

    def set_redis_value(self,key,values):
        """
        根据键值key赋值values
        :param key: 传入键值key
        :param values: 传入需要存储的数据
        :return: 返回赋值成功还是失败的标志
        """
        self.key = key
        self.values = values.encode('utf8')
        try:
            r = redis.Redis(host = self.host, port = self.port, db = 0, password = self.password)
        except Exception as e:
            log_print('Something wrong when connect the redis ...',e)
        try:
            set_res = r.set(self.key, self.values)
        except Exception as e:
            log_print('Update redis values failed ...:',e)
            set_res = False
        return set_res

    def delete_redis_value(self,key):
        """
        根据键值key删除redis的数值
        :param key: 入参为redis的键值
        :return: 返回删除成功还是失败的标志
        """
        self.key = key
        try:
            r = redis.Redis(host = self.host, port = self.port, db = 0, password = self.password)
        except Exception as e:
            log_print('Something wrong when connect the redis ...', e)
        try:
            delete_res = r.delete(self.key)
        except Exception as e:
            log_print('Delete redis values failed ... ', e)
            delete_res = False
        return delete_res

if __name__ == '__main__':
    print('ok')
    # redis_config = GetConfigOperation(config_file).read_redis_config()
    # redis_test = RedisOperation(redis_config.get('host'), redis_config.get('port'), redis_config.get('password'))
    # result = redis_test.get_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(result)
    # set_flag = redis_test.set_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b','19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b2')
    # print(set_flag)
    # result = redis_test.get_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(result)
    # delete_flag = redis_test.delete_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(delete_flag)
    # result = redis_test.get_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(result)