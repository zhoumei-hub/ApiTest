#! /usr/bin/env python3
# -*- coding utf-8 -*-
import re
import config


class GetConfigOperation:

    def __init__(self,config_file):
        self.config_file = config_file

    def config_parsing(self,encoding='utf-8'):
        # pass
        with open(file=self.config_file,mode = 'r',encoding=encoding) as ff:
            content = ff.readlines()
            # print(content)
        return content

    def get_parameter(self):
        """
        解析配置参数，目前只支持$开头的变量
        :param config_content:
        :return:将列表方式返回配置参数，配置参数格式{key:value}
        """
        config_content = self.config_parsing()
        config_data = {}
        total_str = re.compile(r'.+')
        spit_flag = re.compile(r'    ')
        #按照配置文件中的数据逐行解析
        for row_content in config_content:
            #将每行的数据取出，去掉行尾的结束符\n获取每行的字符串
            row_data = total_str.findall(row_content)[0]
            #robot的配置参数是以$开头，解析以$口头的数据，其它的忽略
            # print('\n')
            if row_data[0] == '$':
                # 将每行的字符串进行分割，robot中的配置参数名称，值，备注以四个空格进行分割
                content_split = re.split(spit_flag,row_data)
                # print('the split result is:',content_split)
                # 第一个参数为配置参数名称，第二个参数为配置的值
                key_string = content_split[0]
                value = content_split[1]
                # 将配置参数名称取出，去掉${}
                key = key_string[2:len(key_string) - 1]
                config_data[key] = value
            else:
                pass
        return config_data

    def read_redis_config(self):
        redis_host = self.get_parameter().get('redis_host')
        redis_port = int(self.get_parameter().get('redis_port'))
        redis_password = self.get_parameter().get('redis_password')
        redis_config = {'host':redis_host,'port':redis_port,'password':redis_password}
        return redis_config

    def read_database_config(self):
        database_ip = self.get_parameter().get('database_ip')
        database_port = int(self.get_parameter().get('database_port'))
        database_user = self.get_parameter().get('database_user')
        database_db = self.get_parameter().get('database_db')
        database_password = self.get_parameter().get('database_password')
        run_case_db = self.get_parameter().get('run_case_db')
        database_config = {'host': database_ip, 'port': database_port, 'user': database_user, 'db_name': database_db,'password': database_password,'run_case_db':run_case_db}
        return database_config

    def read_kafka_config(self):
        kafka_host = self.get_parameter().get('kafka_host')
        kafka_port = self.get_parameter().get('kafka_port')
        kafka_config = {'host':kafka_host,'port':kafka_port}
        return kafka_config

    def read_dubbo_config(self):
        test_module_ip = self.get_parameter().get('test_module_ip')
        test_module_port = int(self.get_parameter().get('test_module_port'))
        dubbo_config = {'host':test_module_ip,'port':test_module_port}
        return dubbo_config




if __name__ == '__main__':
    print('ok')
    file = config.CONFIG_FILE
    read_test = GetConfigOperation(file)
    # data = read_test.config_parsing()
    # result = read_test.get_parameter(data)
    kafka_conf = read_test.read_kafka_config()
    print(kafka_conf)
    redis_conf = read_test.read_redis_config()
    print(redis_conf)
    db_config = read_test.read_database_config()
    print(db_config)
    dubbo_config = read_test.read_dubbo_config()
    print(dubbo_config)
