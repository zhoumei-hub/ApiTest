#! /usr/bin/env python3
# -*- coding utf-8 -*-
import pymysql
from logHander import log_print
from config import CONFIG_FILE
from getConfigOperation import GetConfigOperation

class MysqlOperation:
    def __init__(self,host,port,user,password,db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name
    def query_sql(self,sql,args=None):
        """
        查询数据库方法封装
        :param sql:需要执行的查询sql
        :param args:sql中的变量，多个变量放到一个元组中，该处参数可以不传，默认为None
        :return:返回查询状态和查询的结果数据，exec_status为True表示查询成功，False表示查询失败
        """
        conn = pymysql.connect(host = self.host, port = self.port, user = self.user, passwd = self.password, charset = 'utf8',db = self.db_name)
        cursor_sql = conn.cursor()
        try:
            cursor_sql.execute(sql,args)
            query_result = cursor_sql.fetchall()
            log_print('query sql is： :', sql)
            log_print('the query result is:',query_result)
        except Exception as e:
            log_print('something wrong when connect to the :',e)
            query_result = 'query failed'
        finally:
            conn.close()
        return query_result

    def commit_sql(self,sql,args=None):
        """
        对数据库进行增删改方法封装，返回执行状态
        :param sql:需要执行的insert，update，delete语句（sql）
        :param args:sql中的变量，多个变量放到一个元组中，该处参数可以不传，默认为None
        :return:sql执行状态，Ture表示执行成功，False表示查询失败
        """
        conn = pymysql.connect(host = self.host, port = self.port, user = self.user, passwd = self.password, charset = 'utf8',db = self.db_name)
        cursor_sql = conn.cursor()
        try:
            cursor_sql.execute(sql,args)
            conn.commit()
            log_print = 'exec sql successfully :{}'.format(sql)
            exec_result = True
        except Exception as e:
            log_print('something wrong when connect to the :',e)
            conn.rollback()
            exec_result = False
        finally:
            conn.close()
        return exec_result

if __name__ == '__main__':
    print('ok')
    config = GetConfigOperation(CONFIG_FILE)
    database_config = config.read_database_config()
    database_func = MysqlOperation(database_config.get('host'), database_config.get('port'),
                                   database_config.get('user'), database_config.get('password'),
                                   database_config.get('db_name'))


    sql = "select count(1) from t_order_table where phone_number = '13618254716'"
    # sql_use = MysqlOperation()
    resutl = database_func.query_sql(sql)
    print(resutl)
    # sql_update_success = 'update t_execution_table set test_status = 0 where case_id = %s and mock_status = 1'
    # db_config = GetConfigOperation(config_file).read_database_config()
    # print(db_config)
    # db_test = MysqlOperation(db_config.get('host'),db_config.get('port'),db_config.get('user'),db_config.get('password'),db_config.get('db_name'))
    # res = db_test.query_sql(sql)
    # print(res)
    # update_flag = db_test.commit_sql(sql_update_success,'aaa')
    # print(update_flag)
    # db_test =