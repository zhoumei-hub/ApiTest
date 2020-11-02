*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出正在使用的套餐（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100010001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"13618254716","allDevSns":["2059a0caa3d9","cde010000001"]}    13618254716

002_电话号码为空mac码在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100020001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"","allDevSns":["2059a0caa3d9","cde010000001"]}    13618254716

003_请求中只有phone字段没有allDevSns字段（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100030001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"13618254716"}    13618254716

004_请求中只有allDevSns字段没有phone字段（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100040001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"allDevSns":["2059a0caa3d9","cde010000001"]}    13618254716

005_电话号码不在系统中mac码在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100050001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"136182547168","allDevSns":["2059a0caa3d9","cde010000001"]}    "data":[]

006_电话号码在系统中mac码不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100060001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"13618254716","allDevSns":["aaaaa","bbbbb"]}    "data":[]

007_电话号码在系统中mac为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100070001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"13618254716","allDevSns":["",""]}    "data":[]

008_请求中phone对象不正确（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100080001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":[13618254716，],"allDevSns":["2059a0caa3d9","cde010000001"]}    Invalid json argument

009_请求中allDevSns对象不正确（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos100090001    com.cmiot.qos.api.order.QueryUsingOrderService    invoke    {"phone":"13618254716","allDevSns":"2059a0caa3d9"}    "resultCode":"000003"
