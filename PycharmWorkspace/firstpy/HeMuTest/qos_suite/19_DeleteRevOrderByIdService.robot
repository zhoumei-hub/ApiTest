*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功删除关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos190010001    com.cmiot.qos.api.order.DeleteRevOrderByIdService    deleteRevOrderByIdService    9419293    "resultCode":"000000"

001_确认删除待关联订单结果
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

002_id不存在系统中（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos190020001    com.cmiot.qos.api.order.DeleteRevOrderByIdService    deleteRevOrderByIdService    11122233    "resultCode":"000000"

002_确认删除待关联订单结果
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

003_id格式不正确（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos190030001    com.cmiot.qos.api.order.DeleteRevOrderByIdService    deleteRevOrderByIdService    aaabbbccc    Invalid json argument

004_id为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos190040001    com.cmiot.qos.api.order.DeleteRevOrderByIdService    deleteRevOrderByIdService    ""    NumberFormatException

005_请求载荷为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos190050001    com.cmiot.qos.api.order.DeleteRevOrderByIdService    deleteRevOrderByIdService    {}    IllegalArgumentException
