*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询可用优惠券（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos200010001    com.cmiot.qos.api.order.QueryOrderCouponService    invoke    {"orderSerialNumber":"2019090610342904358706"}    2019090610342904358706

002_orderSerialNumber不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos200020001    com.cmiot.qos.api.order.QueryOrderCouponService    invoke    {"orderSerialNumber":"2019090610342904358706aaa"}    "data":[]

003_orderSerialNumber为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos200030001    com.cmiot.qos.api.order.QueryOrderCouponService    invoke    {"orderSerialNumber":""}    "resultCode":"000003"

004_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除可用优惠券}    ${sql_新增可用优惠券}
    [Template]    HemuExecTestCases
    qos200040001    com.cmiot.qos.api.order.QueryOrderCouponService    invoke    {}    "resultCode":"000003"
