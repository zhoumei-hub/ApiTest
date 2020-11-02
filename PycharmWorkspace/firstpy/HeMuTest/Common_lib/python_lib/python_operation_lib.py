#! /usr/bin/env python3
# -*- coding utf-8 -*-

import datetime
from config import CONFIG_FILE
from logHander import log_print
from redisOperation import RedisOperation
from mysqlOperation import MysqlOperation
from kafkaOperation import KafkaOperation
from getConfigOperation import GetConfigOperation
from robotDataOperation import RobotDataOperation

# 获取配置文件
config = GetConfigOperation(CONFIG_FILE)

# 获取redis的配置文件和redis类
redis_config = config.read_redis_config()
redis_func = RedisOperation(redis_config.get('host'), redis_config.get('port'), redis_config.get('password'))

# 获取database的配置文件和database类
database_config = config.read_database_config()
database_func = MysqlOperation(database_config.get('host'),database_config.get('port'),database_config.get('user'),database_config.get('password'),database_config.get('db_name'))

run_case_db_config = config.read_database_config()
run_case_db_func = MysqlOperation(database_config.get('host'),database_config.get('port'),database_config.get('user'),database_config.get('password'),database_config.get('run_case_db'))

run_case_db = database_config.get('run_case_db')


# 获取kafka的配置文件和kafka类
kafka_config = config.read_kafka_config()
kafka_func = KafkaOperation(kafka_config.get('host'), kafka_config.get('port'))

# 获取实现的robot关键字类
robot_func = RobotDataOperation()

# 作为rf的关键字，发送dubbo请求
def python_send_data_func(*point):
    result_to_rf = robot_func.send_data_func(*point)
    return result_to_rf

# 作为rf的关键字，生成dubbo格式的请求
def python_dubbo_request_generate(method,interface_url,payload_flag,payload):
    dubbo_request = robot_func.dubbo_request_generate(method,interface_url,payload_flag,payload)
    return dubbo_request

# 作为rf的关键字，校验测试结果
def python_check_test_result(test_res,expect_res):
    test_result = robot_func.check_test_result(test_res,expect_res)
    return test_result

# 作为rf的关键字，查询数据库
def python_sql_query(sql,args=None):
    if run_case_db in sql:
        print('enter run_case_db')
        query_result = run_case_db_func.query_sql(sql, args)
    else:
        print('enter database_func')
        query_result = database_func.query_sql(sql, args)
    return query_result

# 作为rf的关键字，对数据局进行增删该
def python_sql_commit(sql,args=None):
    if run_case_db in sql:
        commit_result = run_case_db_func.commit_sql(sql, args)
    else:
        commit_result = database_func.commit_sql(sql,args)
    return commit_result

# 作为rf的关键字，查询redis中的数据
def python_get_redis_value(key):
    result = redis_func.get_redis_value(key)
    return result

# 作为rf的关键字，修改/新增redis中的数据
def python_set_redis_value(key,values):
    set_result = redis_func.set_redis_value(key,values)
    return set_result

# 作为rf的关键字，删除redis中的数据
def python_delete_redis_value(key):
    delete_result = redis_func.delete_redis_value(key)
    return delete_result

# 作为rf关键字，向kafka写入数据
def python_kafka_produce_data(topic, send_msg, send_partition):
    produce_result = kafka_func.kafka_produce_data(topic, send_msg, send_partition)
    return produce_result

# 作为rf关键字，读取kafka中待消费的数据
def python_kafka_consume_data(*topic):
    read_data = kafka_func.kafka_consume_data(*topic)
    return read_data

if __name__ == '__main__':
    log_print('Enter python environment')
    # flag = check_running_case()
    # print(flag)
    sql1 = "select count(1) from t_order_table where phone_number = '13618254716'"
    # sql2 = "select * from test.t_user_table"
    sql_result = python_sql_query(sql1)
    print(sql_result)

    # set_res = python_set_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b','osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(set_res)
    # redis_get = python_get_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(redis_get)
    # redis_del = python_delete_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(redis_del)
    # redis_get = python_get_redis_value('osh.app.oprNum_19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b')
    # print(redis_get)
    # ip = '172.19.0.131'
    # port = 20885
    # conn = Dubbo(ip, port)
    # log_print(conn)
    # request = 'invoke com.cmiot.qos.api.order.AddRevOrderService.addRevOrderService({"orderNo":"11122233310","outOrderNo":"abcde123456","phonePay":"13618254716","packageCode":"000111222","areaCode":"023"})'
    # try:
    #     response = conn.do(request)
    #     print(response)
    # except Exception as e:
    #     print('something wrong',e)
    # logfile = 'D:\kouwei\python_worken\\rf_progect\HeMuTest\mylib\python.log'
    # log_output = LogHanderTest(logfile)
    # log_output.logger.info('hello')
    # sql_update_success = 'update t_execution_table set test_status = 0 where case_id = %s and mock_status = 1'
    # case_id = 'qos010010001'
    # test = use_mock_template(case_id)
    # log_print(test)
    # update_status = mysql_commit_sql(sql_update_success, case_id)
    # log_print(update_status)
    # current_time = time.strftime("%Y.%m.%d %H:%M:%S")
    # log_print(current_time)
    # str1 = 'exec sql successfully'
    # log_print(str1[9:21])
    # test_recorde_flag = record_testcase('00013', '1', 'qos', ['qos010010010001','qos010010010002'])
    # str_temp = 'qos010010010002'
    # str_temp = get_module_name('qos010010010002')
    # log_print(str_temp)
    # log_print(test_recorde_flag)
    # # a1 = 'invoke'
    # a4 = '{"userId":"12"}'
    # t = dubbo_request_generate(a1,a2,a3,a4)
    # log_print(t)
    # a2 = 'com.cmiot.qos.api.QueryActiveOrder'
    # a3 = '{"class":"com.cmiot.dhap.core.impl.PoolableBaseContext"}'
    # test = send_data_func('10.11.7.11','20885','0010001', 'invoke com.cmiot.qos.api.QueryActiveOrder.invoke({"class":"com.cmiot.dhap.core.impl.PoolableBaseContext"}{"userId":"12"}) ','1','2' )
    # log_print(test)
    # sql = 'select * from t_order_table where phone_number = %s and id = %s'
    # parmeters = ('13618254716', '18880085')
    # sql1 = 'select count(1) from t_order_table '
    # # parmeters1 = None
    # query_result = python_sql_query(sql, parmeters)
    # log_print(query_result)
    #
    # sql2 = 'update t_order_table set organization_code = %s where phone_number = %s and id = %s'
    # parameter2 = (7001, '13618254716', '18880085')
    # sql3 = 'update t_order_table set organization_code = 7002 where phone_number = 13618254716 and id = 18880085'
    # update_result = mysql_commit_sql(sql3)
    # log_print(update_result)

    # sql4 = "INSERT INTO `platform`.`t_order_table` (`id`, `order_serial_number`, `organization_code`, `phone_number`, `dev_sn`, `package_code`, `effective_time`, `failure_time`, `system_state`, `create_time`, `update_time`, `iscancelled`, `isFromBoss`, `cost`, `orderSource`, `payment_way`) VALUES ('188800853', 'fcha_cdm05', '7002', '13618254716', 'cde010000005', '199020170725000103', '1559318400', '1564588800', '0', '1564476588', '1564476755', NULL, '1', '900', '901', '9')"
    # insert_result = mysql_commit_sql(sql4)
    # log_print(insert_result)
    #
    # sql5 = "delete from t_order_table where phone_number = '13618254716' and id = 188800853"
    # delete_result = mysql_commit_sql(sql5)
    # log_print(delete_result)
    # "resultCode": "000000"