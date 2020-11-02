*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt
Library           ../Common_lib/python_lib/python_lib.py

*** Test Cases ***
001_成功查询出待关联订单(主键查询)（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos060010001    com.cmiot.qos.api.order.QueryRevOrderByIdService    invoke    {"orderId":"9419293"}    9419293

002_关联订单的orderId不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos060020001    com.cmiot.qos.api.order.QueryRevOrderByIdService    invoke    {"orderId":"111222333"}    "resultCode":"000000"

003_关联订单的orderId为空中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos060030001    com.cmiot.qos.api.order.QueryRevOrderByIdService    invoke    {"orderId":""}    "resultCode":"000003"

004_关联订单的请求payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos060040001    com.cmiot.qos.api.order.QueryRevOrderByIdService    invoke    {}    "resultCode":"000003"
