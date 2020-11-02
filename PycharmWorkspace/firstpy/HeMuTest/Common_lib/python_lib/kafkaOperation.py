#! /usr/bin/env python3
# -*- coding utf-8 -*-
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
from logHander import log_print

class KafkaOperation:
    def __init__(self,ip,port):
        self.ip = ip
        self.prot = port
        self.server = ip + ':' +port
    def kafka_produce_data(self,topic, send_msg, send_partition=None):
        """
        实现kafka生产者
        :param topic: 用来接收生产者数据的topic
        :param send_msg: 生产者发送的数据
        :param send_partition: 生产者发送的数据需要存储的partition位置，默认为None，有系统自动分配
        :return: 返回发送结果
        """
        try:
            producer = KafkaProducer(bootstrap_servers=self.server)
            producer.send(topic, send_msg.encode('utf-8'), partition=send_partition)
            send_resut = True
        except KafkaError as e:
            send_resut = False
            log_print('send data wrong ', e)
        finally:
            producer.flush()
            producer.close()
        return send_resut

    def kafka_consume_data(self,*topic):
        """
        实现kafka消费者
        :param topic: 被消费数据的topic，支持传入多个topic进行查询
        :return: 以列表方式返回所查询topic的待消费的数据
        """
        consumer = KafkaConsumer(group_id='test_group', bootstrap_servers=self.server)
        consumer.subscribe(topics=topic)
        poll_num = 5  # 消费者主动消费数据的次数，用来延时，每执行一次延时等待0.2秒
        data_read = []
        try:
            for second_num in range(poll_num):
                msg = consumer.poll(timeout_ms=5)
                if len(msg) > 0:
                    for topic_index in range(len(msg)):
                        #一次拉取会可能会取到多个topic的数据，需要将每个topic中解析出，先转化为列表
                        res_values_temp = list(msg.values())[topic_index]
                        #topic中可能会有多条待消费的数据，需要将每条数据解析出来
                        for data_index in range(len(res_values_temp)):
                            res_value = res_values_temp[data_index].value.decode('utf-8')
                            data_read.append(res_value)
                time.sleep(0.2)
        except Exception as e:
            log_print('receive data error', e)
        finally:
            consumer.commit()
            consumer.close()
        return data_read

if __name__ == '__main__':
    print('ok')
    # test = KafkaOperation('172.19.0.131','9092')
    # topic_1 = 'koutest'
    # topic_2 = 'koutest2'
    # send_msg = 'I am python producer,sent data to '
    # kafka_config = GetConfigOperation(config_file).read_kafka_config()
    # kafka_test = KafkaOperation(kafka_config.get('host'), kafka_config.get('port'))
    # for i in range(5):
    #     send_res = kafka_test.kafka_produce_data(topic_1,send_msg + topic_1)
    #     log_print(send_res)
    # for i in range(2):
    #     send_res = kafka_test.kafka_produce_data(topic_2,send_msg + topic_2)
    #     log_print(send_res)
    # consumer_data = kafka_test.kafka_consume_data(topic_1,topic_2)
    # log_print(consumer_data)