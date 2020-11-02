*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_操作码未重复返回成功（Redis正）
    [Setup]    hemu_set_redis_value    &{CheckOperationCode}
    [Template]    HemuExecTestCases
    qos070010001    com.cmiot.qos.api.operation.CheckOperationCode    invoke    {"code":"19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b"}    "resultCode":"000000"

002_操作码code不在缓存中（Redis反）
    [Setup]    hemu_del_redis_value    &{CheckOperationCode}[key]
    [Template]    HemuExecTestCases
    qos070020001    com.cmiot.qos.api.operation.CheckOperationCode    invoke    {"code":"19926359:2059a0caa3d9:39_month_7_01:a1d263f249e54b4fbb0243da8352328b"}    "resultCode":"000001"

003_操作码code为空（Redis反）
    [Setup]    hemu_set_redis_value    &{CheckOperationCode}
    [Template]    HemuExecTestCases
    qos070030001    com.cmiot.qos.api.operation.CheckOperationCode    invoke    {"code":""}    "resultCode":"000003"

004_请求载荷payload为空（Redis反）
    [Setup]    hemu_set_redis_value    &{CheckOperationCode}
    [Template]    HemuExecTestCases
    qos070040001    com.cmiot.qos.api.operation.CheckOperationCode    invoke    {}    "resultCode":"000003"
