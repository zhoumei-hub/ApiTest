*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_查询出待关联订单数（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联订单--无mac}
    [Template]    HemuExecTestCases
    qos170010001    com.cmiot.qos.api.order.QueryRevOrderCountService    invoke    {"phone":13618254716}    {"totalNum":1}

002_待关联套餐不存在（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos170020001    com.cmiot.qos.api.order.QueryRevOrderCountService    invoke    {"phone":13618254716}    {"totalNum":0}

003_phone不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos170030001    com.cmiot.qos.api.order.QueryRevOrderCountService    invoke    {"phone":11122223333}    {"totalNum":0}

004_phone不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos170040001    com.cmiot.qos.api.order.QueryRevOrderCountService    invoke    {"phone":""}    "resultCode":"000003"

005_查询请求载荷为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos170050001    com.cmiot.qos.api.order.QueryRevOrderCountService    invoke    {}    "resultCode":"000003"
