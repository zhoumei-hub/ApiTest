*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出生效的套餐(主键查询)（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos080010001    com.cmiot.qos.api.order.QueryUsingOrderByIdService    invoke    {"orderId":"100000441381"}    100000441381

002_请求中orderId不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos080020001    com.cmiot.qos.api.order.QueryUsingOrderByIdService    invoke    {"orderId":"11222333444"}    resultCode":"000000

003_请求中orderId为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos080030001    com.cmiot.qos.api.order.QueryUsingOrderByIdService    invoke    {"orderId":""}    "resultCode":"000003"

004_请求负载payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos080040001    com.cmiot.qos.api.order.QueryUsingOrderByIdService    invoke    {}    "resultCode":"000003"
