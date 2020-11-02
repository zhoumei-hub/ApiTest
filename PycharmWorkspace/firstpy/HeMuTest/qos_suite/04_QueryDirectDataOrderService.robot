*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功返回专属流量套餐（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除专属流量套餐}    ${sql_新增专属流量套餐}
    [Template]    HemuExecTestCases
    qos040010001    com.cmiot.qos.api.order.QueryDirectDataOrderService    invoke    {"phoneNum":"13618254716"}    13618254716

002_电话号码为空--查询全部（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除专属流量套餐}    ${sql_新增专属流量套餐}
    [Template]    HemuExecTestCases
    qos040020001    com.cmiot.qos.api.order.QueryDirectDataOrderService    invoke    {"phoneNum":""}    13618254716

003_查询请求payload为空--查询全部（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除专属流量套餐}    ${sql_新增专属流量套餐}
    [Template]    HemuExecTestCases
    qos040030001    com.cmiot.qos.api.order.QueryDirectDataOrderService    invoke    {}    13618254716

004_电话号码不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除专属流量套餐}    ${sql_新增专属流量套餐}
    [Template]    HemuExecTestCases
    qos040040001    com.cmiot.qos.api.order.QueryDirectDataOrderService    invoke    {"phoneNum":"136182547168"}    "data":[]
