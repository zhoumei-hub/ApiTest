*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_根据全部条件查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300010001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9","orderSerialNumber":"2019081909025205206222","phoneNumber":"13618254716"}    13618254716

002_根据phoneNumber&devSn查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300020001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9","phoneNumber":"13618254716"}    13618254716

003_根据phoneNumber&orderSerialNumber查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300030001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"orderSerialNumber":"2019081909025205206222","phoneNumber":"13618254716"}    13618254716

004_根据devSn&orderSerialNumber查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300040001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9","orderSerialNumber":"2019081909025205206222"}    13618254716

005_根据phoneNumber查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300050001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"phoneNumber":"13618254716"}    13618254716

006_根据orderSerialNumber查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300060001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"orderSerialNumber":"2019081909025205206222"}    13618254716

007_根据orderSerialNumber查询出订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300070001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9"}    13618254716

008_devSn不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300080001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"aaabbbccc","orderSerialNumber":"2019081909025205206222","phoneNumber":"13618254716"}    "data":[]

009_orderSerialNumber不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300090001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9","orderSerialNumber":"201908191111111111111","phoneNumber":"13618254716"}    "data":[]

010_phoneNumber不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300100001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"devSn":"2059a0caa3d9","orderSerialNumber":"2019081909025205206222","phoneNumber":"12345678910"}    "data":[]

011_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos300110001    com.cmiot.qos.api.order.QueryOrderByConditionService    invoke    {"此处应该报错，但是却查询出默认订单"}    "resultCode":"000003"
