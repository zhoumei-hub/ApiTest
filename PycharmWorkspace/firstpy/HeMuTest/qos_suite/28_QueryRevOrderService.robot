*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_phone查询出1条待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280010001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {"phone":"13618254716","page":"1"}    13618254716

002_phone不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280020001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {"phone":"12345678910","page":"1"}    "data":[]

003_phone为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280030001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {"phone":"","page":"1"}    "resultCode":"000003"

004_page为空，查出全部订单 （正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280040001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {"phone":"13618254716","page":""}    13618254716

005_page格式错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280050001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {"phone":"13618254716","page":"aaabbb"}    "resultCode":"000003"

006_请求载荷为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos280050001    com.cmiot.qos.api.order.QueryRevOrderService    invoke    {}    "resultCode":"000003"
