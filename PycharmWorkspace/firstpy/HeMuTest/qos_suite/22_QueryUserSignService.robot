*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出用户签约状态（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220010001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {phoneNum:13618254716,paymentWay:1}    13618254716

002_phoneNum不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220020001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {phoneNum:12345678910,paymentWay:1}    "resultCode":"000000"

003_phoneNum为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220030001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {"phoneNum":"","paymentWay":"1"}    "resultCode":"000003"

004_phoneNum字段缺失（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220040001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {paymentWay:1}    "resultCode":"000003"

005_paymentWay不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220050001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {"phoneNum":"13618254716","paymentWay":"aabbcc"}    "data":[]

006_paymentWay为空--查全部（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220060001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {"phoneNum":"13618254716","paymentWay":""}    13618254716

007_paymentWay字段缺失--查全部（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220070001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {"phoneNum":"13618254716"}    13618254716

008_请求报文载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除签约订单}    ${sql_新增签约订单}
    [Template]    HemuExecTestCases
    qos220080001    com.cmiot.qos.api.order.QueryUserSignService    invoke    {}    "resultCode":"000003"
