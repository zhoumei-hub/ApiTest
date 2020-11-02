*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_电话号码和mac码都在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050010001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"13618254716","allDevSns":["2059a0caa3d9","cde010000001"]}    13618254716

002_电话号码不在系统中和mac码在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050020001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"12345678910","allDevSns":["2059a0caa3d9",""]}    13618254716

003_电话号码在系统中和mac码不在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050030001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"13618254716","allDevSns":["aaaaa","bbbbb"]}    13618254716

004_电话号码和mac码都不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050040001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"12345678910","allDevSns":["aaaaa","bbbbb"]}    "data":[]

005_电话号码phone为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050050001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"","allDevSns":["aaaaa","bbbbb"]}    "resultCode":"000003"

006_设备码allDevSns类型错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050060001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":"13618254716","allDevSns":""}    "resultCode":"000003"

007_设备码phone类型错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050070001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {"phone":["13618254716"],"allDevSns":""}    "resultCode":"000003"

008_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos050080001    com.cmiot.qos.api.order.QueryActOrdByPhoneAndMacService    invoke    {}    "resultCode":"000003"
