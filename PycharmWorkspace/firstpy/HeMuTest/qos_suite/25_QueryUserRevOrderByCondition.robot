*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_phonePay成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250010001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"","outOrderNo":"",phonePay:"13618254716"}    13618254716

002_devSn成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250020001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"2059a0caa3d9","outOrderNo":"",phonePay:""}    13618254716

003_devSn成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250030001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"","outOrderNo":"fcha_cdm05",phonePay:""}    13618254716

004_phonePay&fcha_cdm05成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250040001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"","outOrderNo":"fcha_cdm05",phonePay:"13618254716"}    13618254716

005_devSn&phonePay成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250050001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"2059a0caa3d9","outOrderNo":"",phonePay:"13618254716"}    13618254716

006_devSn&outOrderNo成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250060001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"2059a0caa3d9","outOrderNo":"fcha_cdm05",phonePay:""}    13618254716

007_devSn&outOrderNo&phonePay成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250070001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"","devSn":"2059a0caa3d9","outOrderNo":"fcha_cdm05",phonePay:"13618254716"}    13618254716

008_devSn&outOrderNo&phonePay&state成功查询出待关联订单（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250080001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"0","devSn":"2059a0caa3d9","outOrderNo":"fcha_cdm05",phonePay:"13618254716"}    13618254716

009_state不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250090001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"99","devSn":"2059a0caa3d9","outOrderNo":"fcha_cdm05",phonePay:"13618254716"}    data":[]

010_state格式不正确（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250100001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"state":"aabbcc","devSn":"2059a0caa3d9","outOrderNo":"fcha_cdm05",phonePay:"13618254716"}    "resultCode":"000003"

011_载荷payload为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除待关联套餐}    ${sql_新增待关联套餐}
    [Template]    HemuExecTestCases
    qos250110001    com.cmiot.qos.api.order.QueryUserRevOrderByCondition    invoke    {"此处载荷为空无法返回响应，建议走查代码"}    "resultCode":"000000"
