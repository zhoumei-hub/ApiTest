*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出状态为1的待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos230010001    com.cmiot.qos.api.order.QueryAllRevOrderByConditionService    invoke    {state:0}    13618254716

002_state值不在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos230020001    com.cmiot.qos.api.order.QueryAllRevOrderByConditionService    invoke    {state:111}    "data":[]

003_state值为空（正）
    [Tags]    qos
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    [Timeout]    5 seconds
    qos230030001    com.cmiot.qos.api.order.QueryAllRevOrderByConditionService    invoke    {"state":"此处为空的时候无法返回结果，需要走查源码"}    "resultCode":"000000"

004_state值类型错误（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos230040001    com.cmiot.qos.api.order.QueryAllRevOrderByConditionService    invoke    {"state":"aaabbb"}    "resultCode":"000003"

005_请求载荷payload为空（正）
    [Tags]    qos
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    [Timeout]    5 seconds
    qos230050001    com.cmiot.qos.api.order.QueryAllRevOrderByConditionService    invoke    {"此处为空的时候无法返回结果，需要走查源码"}    "resultCode":"000000"
