#! /usr/bin/env python3
# -*- coding utf-8 -*-
import re
import time
from logHander import log_print
from config import CONFIG_FILE
from dubboOperation import DubboOperation
from mysqlOperation import MysqlOperation
from getConfigOperation import GetConfigOperation

# 获取配置文件
config = GetConfigOperation(CONFIG_FILE)
# 获取database的配置文件和database类
run_case_db = config.read_database_config()
run_case_db_func = MysqlOperation(run_case_db.get('host'),run_case_db.get('port'),run_case_db.get('user'),run_case_db.get('password'),run_case_db.get('run_case_db'))

# 获取dubbo的配置文件和database类
# dubbo_config = config.read_dubbo_config()
# dubbo_func = DubboOperation(dubbo_config.get('host'),dubbo_config.get('port'))

# # 获取redis的配置文件和redis类
# redis_config = config.read_redis_config()
# redis_func = RedisOperation(redis_config.get('host'), redis_config.get('port'), redis_config.get('password'))

# 获取kafka的配置文件和kafka类
# kafka_config = config.read_kafka_config()
# kafka_func = KafkaOperation(kafka_config.get('host'), kafka_config.get('port'))


class RobotDataOperation:

    def send_data_func(self,*point):
        """
        封装成关键字，用来发送dubbo请求
        :param ip:dubbo服务的IP
        :param port: dubbo服务的端口
        :param request: rf下发的请求，此处的请求由三部分组成${id}，${dubbo_request}，@{mock_data}
        :return:返回dubbo_response响应，判断测试结果
        """
        log_print('------------------ python received testcase ------------------')
        log_print('python receive message :', point)
        data_num = len(point)
        # ip = point[0]
        # port = point[1]
        test_case_id = point[0]
        dubbo_request = point[1]  # 真正的dubbo请求
        if data_num > 2:
            mock_data = point[2:data_num]
        else:
            mock_data = ['0', ]
        test_module = self.get_module_name(test_case_id)  # 根据传入的case_id取出其中的字符，组成module的名称
        # 判断是否满足向dubbo发送请求的条件
        send_flag, case_mock_flag = self.send_data_ready(test_case_id, test_module, mock_data)
        if send_flag is True:
            dubbo_config = config.read_dubbo_config()
            dubbo_func = DubboOperation(dubbo_config.get('host'), dubbo_config.get('port'))
            # conn = DubboOperation(ip, port)
            # log_print(conn)
            try:
                log_print('receive the dubbo request ...')
                dubbo_response = dubbo_func.do(dubbo_request)
                log_print('wait dubbo return ', dubbo_response)
                # 此处成功收到dubbo服务的响应，需要判断需要mock模板数据的是否成功的被使用
                log_print('response_return test_case_id is : ', test_case_id)
                result_to_rf = self.response_return(test_case_id, case_mock_flag, dubbo_response)
            except Exception as e:
                log_print('connect the dubbo failed:', e)
                result_to_rf = 'connect the dubbo failed'
        else:
            result_to_rf = 'send_flag is False,can not send to dubbo '
        log_print('------------------ python return result ------------------')
        return result_to_rf

    # 从传入的case_id中解析出模块名称来，模块名必须小写
    def get_module_name(self,case_id):
        str_temp = re.findall(r'[a-z]', case_id)
        module = ''.join(str_temp)
        return module

    def send_data_ready(self,case_id, test_module, mock_ids):
        """
        # 判断是否能否向dubbo发送数据，如果需要使用mock模板的数据，则需要先录入数据库，如果不需要直接发送
        :param case_id: 执行的测试用例id
        :param test_module: 被测试的模块
        :param mock_ids: 需要被mock的数据
        :return: ready_flag =1 表示完成准备工作，可以发送dubbo请求了。mock_flag = 1 表示该用例需要用到
        """
        log_print('judge whether need the mock data:', mock_ids[0])
        log_print('the mock_id flag is:', mock_ids[0])
        if mock_ids[0] == '0':
            # 判断是否需要调用mock模板，如果mock_id的值为0，表示不需要mock模板，也就不需要记录到数据库中
            mock_flag = 0
            ready_flag = True
        else:
            # 如果需要调用mock模板的数据，先将数据插入到数据库中，供mock平台使用
            log_print("Need the mook data ...")
            ready_flag = self.record_testcase(case_id, test_module, mock_ids)
            mock_flag = 1
        return ready_flag, mock_flag

    def response_return(self,case_id, mock_flag, dubbo_response):
        """
        # mock_flag=0没有使用mock模板，直接返回给rf，case_mock_flag=1需要先校验数据库里面的状态是否变更为已经使用
        :param mock_flag: 是否需要mock的标志位
        :param response: dubbo服务返回的结果
        :return: 最终返回给rf的响应内容
        """
        log_print('begin to return the mock data from db ... ')
        log_print('the test case is : ', case_id)
        sql_update_success = 'update t_execution_table set test_status = 0 where case_id = %s and  mock_status = 0'
        if mock_flag == 0:
            # 不需要mock模板数据，直接返回
            log_print('No need to use mock data,return ...')
            result_temp = dubbo_response
        elif mock_flag == 1:
            log_print('Need to use mock data ....')
            # 使用了mock模板，需要先判断是mock模板是否全部被成功调用了
            if self.use_mock_template(case_id) is True:
                log_print('update step sql_update_success:', sql_update_success)
                log_print('update step case_id', case_id)
                update_res = run_case_db_func.commit_sql(sql_update_success, case_id)
                # update_status = update_res[9:21]
                update_status = update_res
                # if update_status == 'successfully':
                if update_status is True:
                    log_print('update the test_status successfully')
                else:
                    log_print('update the test_status failed')
                # 不论更新test_staus成功还是失败，都给rf返回dubbo的响应
                result_temp = dubbo_response
            else:
                log_print('need the mock template,but one or more template is not used ')
                result_temp = 'need the mock template,but one or more template is not used'
        else:
            result_temp = 'case_mock_flag return wrong '
        return result_temp

    # 收到rf发来的报文（需要mock的），需要把数据插入到数据库中再发送dubbo
    def record_testcase(self,case_id, test_module, mock_ids):
        """
        收到rf发来的报文（需要mock的），需要把数据插入到数据库中再发送dubbo
        此处只执行一条insert语句，返回该条语句执行的结果
        :param case_id: 测试用例编号
        :param step: 该测试用例中需要用到的模拟接口数据（第几个）
        :param test_module: 被测试模块
        :param mock_id: 需要用到的模拟接口数据模板,此处可能是多个模板，必须传入一个list链表
        :return:返回当前insert执行结果，True全部成功，Flase有执行失败的语句。
        """
        log_print('begin to record the test case into database')
        insert_result = []
        data_len = len(mock_ids)
        log_print('the mock template id is :', mock_ids)
        run_flag = self.check_running_case()
        if run_flag is True:
            current_time = time.strftime("%Y.%m.%d %H:%M:%S")
            # 先将数据库中相同caseid的执行记录删除,保证相同的用例可以重复执行
            sql_del = "delete from t_execution_table where case_id = %s"
            del_result = run_case_db_func.commit_sql(sql_del, case_id)
            log_print(del_result)
            # 开始插入测试条目
            sql = 'insert into t_execution_table (case_id,step,test_module,mock_id,mock_status,test_status,create_time)VALUES ( %s,%s,%s,%s,1,1,%s)'
            for i in range(data_len):
                log_print('the mock template id is :', mock_ids[i])
                sql_parameters = (case_id, i + 1, test_module, mock_ids[i], current_time)
                exce_result = run_case_db_func.commit_sql(sql, sql_parameters)
                log_print(exce_result)
                # log_print(exce_result[9:21])
                if exce_result is True:
                    exce_flag = 'successfully'
                else:
                    exce_flag = 'failed'
                insert_result.append(exce_flag)  # 将每条insert执行的结果放入到列表中，用来判断是否所有的模板都被插入数据库中
            log_print(insert_result)
            num = str(insert_result).count("successfully")  # 计算执行insert成功的次数
            log_print(num)
            if num == data_len:
                rescord_result = True
            else:
                rescord_result = False
        else:
            rescord_result = False
            log_print('Please wait a while,someone is running the testcase at the same time ')
        return rescord_result

    def use_mock_template(self,case_id):
        """
        在返回给rf之前，先判断是否需要mock模板数据，如果需要则判断数据库中的模板数据是否被使用过
        :param case_id: 正在执行的测试用例
        :return: False表示查询是否使用模板失败了或者模板数据未被全部使用，True表示模板数据被成功使用
        """
        log_print('Begin to user query the mock data')
        sql_mock_total = "select count(1) from t_execution_table where case_id = %s and test_status = 1"
        sql_mock_succuss = "select count(1) from t_execution_table where case_id = %s and mock_status = 0"
        mock_total_res = run_case_db_func.query_sql(sql_mock_total, case_id)
        mock_succuss_res = run_case_db_func.query_sql(sql_mock_succuss, case_id)
        if mock_total_res == 'query failed':
            log_print('query failed .the sql is %s:', sql_mock_total)
            return False
        else:
            log_print('Query the mock_data successfully...')
            mock_total_num = mock_total_res[0][0]
            mock_succuss_num = mock_succuss_res[0][0]
            if mock_total_num == mock_succuss_num:
                log_print('mock_total_num is :', mock_total_num)
                log_print('mock_succuss_num is :', mock_succuss_num)
                log_print('all the mock template is used successfully .')
                return True
            else:
                log_print('mock_total_num is :', mock_total_num)
                log_print('mock_succuss_num is :', mock_succuss_num)
                log_print('something wrong ,the mock template is not used all .')
                return False

    def check_running_case(self):
        sql = "select count(1) from t_execution_table where mock_status = 1"
        running_num = run_case_db_func.query_sql(sql)
        print(running_num)
        if running_num[0][0] == 0:
            res = True
        else:
            res = False
            log_print('Please wait a while,someone is running the testcase at the same time ')
        return res

    def dubbo_request_generate(self,method,interface_url,payload_flag,payload):
        """
        根据输入的负载，生成最终的dubbo请求，通过python_fun发送到dubbo服务
        :param method:需要测试的方法
        :param interface_url:接口的url
        :param payload_flag:每个dubbo请求中默认的前缀
        :param payload:每个dubbo真实的载荷
        :return:
        """
        if method.replace(' ','') == 'invoke':
            dubbo_request = 'invoke' + ' ' + interface_url.replace(' ', '') + '.' + method.replace(' ', '') + '(' + payload_flag.replace(' ','') + payload.replace(' ','') + ')'
        else:
            dubbo_request = 'invoke' + ' ' + interface_url.replace(' ', '') + '.' + method.replace(' ', '') +  '(' + payload.replace(' ', '') + ')'
        return dubbo_request

    def check_test_result(self,test_res, expect_res):
        count = 0
        expect_str_list = expect_res.replace(' ', '').split('|')
        for expect_str in expect_str_list:
            if expect_str in test_res.replace(' ', ''):
                pass
            else:
                log_print('{} is not in actual result '.format(expect_str))
                count += 1
        return count