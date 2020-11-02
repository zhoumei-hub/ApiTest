*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功生成操作码（Redis正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos110010001    com.cmiot.qos.api.operation.GenerateOperationCode    invoke    {"item":"39_month_7_01","userId":"19926359","mac":"2059a0caa3d9"}    "resultCode":"000000"

002_item字段为空（Redis正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos110020001    com.cmiot.qos.api.operation.GenerateOperationCode    invoke    {"item":"","userId":"19926359","mac":"2059a0caa3d9"}    "resultCode":"000000"

003_userId字段为空（Redis反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos110030001    com.cmiot.qos.api.operation.GenerateOperationCode    invoke    {"item":"39_month_7_01","userId":"","mac":"2059a0caa3d9"}    "resultCode":"000003"

004_mac字段为空（Redis反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos110040001    com.cmiot.qos.api.operation.GenerateOperationCode    invoke    {"item":"39_month_7_01","userId":"19926359","mac":""}    "resultCode":"000003"

005_请求payload为空（Redis反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos110040001    com.cmiot.qos.api.operation.GenerateOperationCode    invoke    {}    "resultCode":"000003"
