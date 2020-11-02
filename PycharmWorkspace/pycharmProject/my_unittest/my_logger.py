"""
======================
输出日志
在控制台和文件中输出
======================
"""

import logging
from my_unittest.handle_config import conf


class MyLogger(logging.Logger):


    def __init__(self,file=None):
        # 设置输出级别、输出渠道、输出日志格式
        # super().__init__(name,level)
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))
        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log","file_ok"):
    file_name = conf.get("log","file_name")
else:
    file_name = None

# mlogger = MyLogger(conf.get("log","name"),file=file_name)
mlogger = MyLogger(file_name)

if __name__ == '__main__':
    mlogger = MyLogger("py30",file="my_logger.log")
    mlogger.info("测试，我自己封装的日志类！！！！")