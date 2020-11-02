*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出临时订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除临时订单}    ${sql_新增临时订单}
    [Template]    HemuExecTestCases
    qos090010001    com.cmiot.qos.api.order.QueryTempOrderService    invoke    {"orderSerialNumber":"2019081909025205206222"}    2019081909025205206222
