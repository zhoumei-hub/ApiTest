*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_没有冻结套餐（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除冻结套餐}
    [Template]    HemuExecTestCases
    qos160010001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":"2059a0caa3d9"}    "frozenFlag":0

002_成功查询出冻结套餐（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除冻结套餐}    ${sql_新增冻结套餐}
    [Template]    HemuExecTestCases
    qos160020001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":"2059a0caa3d9"}    "frozenFlag":1

003_成功查询出冻结套餐mac大写（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除冻结套餐}    ${sql_新增冻结套餐}
    [Template]    HemuExecTestCases
    qos160030001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":"2059A0CAA3D9"}    "frozenFlag":1

004_mac不存在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除冻结套餐}    ${sql_新增冻结套餐}
    [Template]    HemuExecTestCases
    qos160040001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":"aaabbbccc"}    "frozenFlag":0

005_mac为空（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除冻结套餐}    ${sql_新增冻结套餐}
    [Template]    HemuExecTestCases
    qos160050001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":""}    "resultCode":"000003"

006_请求载荷payload为空（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除冻结套餐}    ${sql_新增冻结套餐}
    [Template]    HemuExecTestCases
    qos160060001    com.cmiot.qos.api.order.CheckOrderFrozenByMac    invoke    {"mac":""}    "resultCode":"000003"
