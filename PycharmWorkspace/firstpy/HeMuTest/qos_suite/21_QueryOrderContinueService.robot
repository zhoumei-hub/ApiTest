*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功用户套餐续费订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除续费订单}    ${sql_新增续费订单}
    [Template]    HemuExecTestCases
    qos210010001    com.cmiot.qos.api.order.QueryOrderContinueService    invoke    {"orderId":"1360012121302537"}    2019071017395139443039

002_orderId不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除续费订单}    ${sql_新增续费订单}
    [Template]    HemuExecTestCases
    qos210020001    com.cmiot.qos.api.order.QueryOrderContinueService    invoke    {"orderId":"aaabbbccc"}    "resultCode":"000000"

003_orderSerialNumber为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除续费订单}    ${sql_新增续费订单}
    [Template]    HemuExecTestCases
    qos210030001    com.cmiot.qos.api.order.QueryOrderContinueService    invoke    {"orderId":""}    "resultCode":"000003"

004_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除续费订单}    ${sql_新增续费订单}
    [Template]    HemuExecTestCases
    qos210040001    com.cmiot.qos.api.order.QueryOrderContinueService    invoke    {}    "resultCode":"000003"
