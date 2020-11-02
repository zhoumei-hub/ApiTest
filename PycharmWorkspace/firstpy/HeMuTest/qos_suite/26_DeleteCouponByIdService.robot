*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_通过主键删除可用优惠券（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos260010001    com.cmiot.qos.api.order.DeleteCouponByIdService    deleteCouponByIdService    2804    "resultCode":"000000"

001_确认删除成功
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

002_主键不存在系统中（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos260020001    com.cmiot.qos.api.order.DeleteCouponByIdService    deleteCouponByIdService    00001    data":null

002_确认没有删除
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

003_主键为空字符串（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos260030001    com.cmiot.qos.api.order.DeleteCouponByIdService    deleteCouponByIdService    ""    NumberFormatException

003_确认没有删除
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

004_主键格式错误（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos260020001    com.cmiot.qos.api.order.DeleteCouponByIdService    deleteCouponByIdService    aabbcc    Unexcepted token expect

004_确认没有删除
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1
