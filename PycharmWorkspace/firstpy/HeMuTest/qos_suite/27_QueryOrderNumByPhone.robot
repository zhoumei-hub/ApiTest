*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_phoneNumber查询出全部订单（正）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270010001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {"phoneNumber":"13618254716","organizationCode":"","packageCode":""}    fcha_cdm05

002_phoneNumber&packageCode查询出全部订单（正）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270020001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {"phoneNumber":"13618254716","organizationCode":"","packageCode":"199020170725000103"}    fcha_cdm05

003_organizationCode不存在系统中（反）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270030001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {"phoneNumber":"13618254716","organizationCode":"aaa","packageCode":"199020170725000103"}    "resultCode":"000003"

004_通过packageCode查询订单（反）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270040001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {"phoneNumber":"","":"aaa","packageCode":"199020170725000103"}    "resultCode":"000003"

005_都未空时查询（反）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270050001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {"phoneNumber":"","":"aaa","packageCode":""}    "resultCode":"000003"

006_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除已激活订单}    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos270060001    com.cmiot.qos.api.order.QueryOrderNumByPhone    invoke    {}    "resultCode":"000003"
