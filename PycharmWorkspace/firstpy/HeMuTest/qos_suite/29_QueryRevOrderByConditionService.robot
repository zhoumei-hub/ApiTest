*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_根据条件phone&devSnList&state查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290010001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","devSnList":["2059a0caa3d9"],"state":"0"}    13618254716

002_根据条件phone查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290020001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716"}    13618254716

003_根据条件phone&devSnList查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290030001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","devSnList":["2059a0caa3d9"]}    13618254716

004_根据条件phone&state查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290040001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","state":"0"}    13618254716

005_devSnList不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290050001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","devSnList":["aaabbbccc"]}    "data":[]

006_state不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290060001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","state":"111"}    "data":[]

007_state格式不正确（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290070001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"13618254716","state":"aaabbb"}    "resultCode":"000003"

008_phone不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290080001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {"phone":"12345678910","devSnList":["2059a0caa3d9"],"state":"0"}    "data":[]

009_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos290100001    com.cmiot.qos.api.order.QueryRevOrderByConditionService    invoke    {}    "resultCode":"000003"
