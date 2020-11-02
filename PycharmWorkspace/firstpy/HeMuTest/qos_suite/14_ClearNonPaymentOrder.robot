*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_清理临时订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140010001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"userId":"19759589","devices":["2059a0caa3d9"]}    "resultCode":"000000"
    [Teardown]

001_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    3
    [Teardown]

002_无userId清理临时订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140020001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"devices":["2059a0caa3d9"]}    "resultCode":"000000"
    [Teardown]

002_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    3

003_无devices清理临时订单（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140030001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"userId":"19759589"}    "resultCode":"000003"
    [Teardown]

003_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    2

004_无devices清理临时订单（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140040001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"userId":"19759589"}    "resultCode":"000003"
    [Teardown]

004_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    2

005_devices格式异常（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140050001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"devices":"2059a0caa3d9"}    "resultCode":"000003"
    [Teardown]

005_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    2

006_devices大小写不敏感（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos140060001    com.cmiot.qos.api.ClearNonPaymentOrder    invoke    {"devices":["2059A0CAA3d9"]}    "resultCode":"000000"
    [Teardown]

006_确认清理结果
    [Template]    hemu_query_db_result
    ${sql_查询临时表清理结果}    3
