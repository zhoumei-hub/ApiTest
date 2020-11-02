*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出该mac下可用订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos120010001    com.cmiot.qos.api.order.QueryAvailableOrderByMac    invoke    {"mac":"2059a0caa3d9"}    "2019081909025205206222"

002_mac码不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos120020001    com.cmiot.qos.api.order.QueryAvailableOrderByMac    invoke    {"mac":"aaabbbcccdd"}    "data":[]

003_mac码为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos120030001    com.cmiot.qos.api.order.QueryAvailableOrderByMac    invoke    {"mac":""}    "resultCode":"000003"

004_查询请求为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos120040001    com.cmiot.qos.api.order.QueryAvailableOrderByMac    invoke    {}    "resultCode":"000003"
