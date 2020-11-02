#! /usr/bin/env python3
# -*- coding utf-8 -*-
import telnetlib
import socket
#通过telnet对dubbo服务发送请求
class DubboOperation(telnetlib.Telnet):
    """
    封装一个telnet访问dubbo的类，用来发送请求
    """
    prompt = 'dubbo>'
    # coding = 'utf-8'
    coding = 'gbk'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=""):
        self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        data = self.read_until(flag.encode())
        self.close()
        return data

    def do(self, arg):
        command_str = arg
        res = self.command(DubboOperation.prompt, command_str)
        res_data = res.decode(DubboOperation.coding,errors='ignore').split('\n')[0].strip()
        return res_data
    def dubbo_closed(self):
        self.close()