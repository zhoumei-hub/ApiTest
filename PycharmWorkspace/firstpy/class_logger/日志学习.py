"""
======================
Author: 柠檬班-小简
Time: 2020/6/17 20:38
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
logging模块！！
                          =》日志级别。
             渠道2(Handle) =》日志格式(Formatter)。
日志收集器 =》 渠道1(Handle) =》日志格式(Formatter)。
                          =》日志级别。
             日志级别


0、日志收集器：

1、日志级别(Level)：DEBUG、INFO、WARNING、ERROR、CRITICAL(FATAL)
2、输出渠道(Handle)：控制台(StreamHandle)、文件(FileHandle)。
3、日志内容(Format)：时间-哪个文件-哪行代码-输出内容

logging模块，默认的root日志收集器。默认的输出级别：WARNING

第一步：
创建一个日志收集器：logging.getLogger("收集器的名字")

第二步：
给日志收集器，设置日志级别：logger.setLevel(logging.INFO)

第三步：
给日志收集器，创建一个输出渠道。handle1 = logging.StreamHandler()

第四步：
给渠道，设置一个日志输出内容的格式。

第五步：
将设置的格式，绑定到渠道当中。将格式与渠道关联起来。

第六步：
将设置好的渠道，添加到日志收集器上。

"""
import logging

# logging.info("hello,py30,第一次日志输出操作！！")
logging.warning("hello,py30,第一次警告级别的日志输出操作！！")


logger = logging.getLogger("nmb-py30")
# 设置日志输出级别。
logger.setLevel(logging.INFO)

# 设置日志输出在哪些渠道
handle1 = logging.StreamHandler()
# 设置渠道自己的输出级别。
handle1.setLevel(logging.ERROR)

# 设置渠道的输出内容格式
fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
formatter = logging.Formatter(fmt)

# 将日志格式绑定到渠道当中。
handle1.setFormatter(formatter)

# 第六步：
# 将设置好的渠道，添加到日志收集器上。
logger.addHandler(handle1)

# 添加fileHandle
handle2 = logging.FileHandler("my_py30.log",encoding="utf-8")
handle2.setFormatter(formatter)
logger.addHandler(handle2)


logger.info("hello,py30,我的第一个收集器设置成功了吗？？")
logger.error("ERRor1111!!!!!")

from logging import handlers