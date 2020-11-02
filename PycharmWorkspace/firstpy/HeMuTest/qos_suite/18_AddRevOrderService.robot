*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功生成关联订单（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180010001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"orderNo":"11122233310","outOrderNo":"abcde123456","phonePay":"13618254716","packageCode":"000111222","areaCode":"023"}    "resultCode":"000000"

001_确认待关联表生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    1

002_orderNo字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180020001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"outOrderNo":"abcde123456","phonePay":"13618254716","packageCode":"000111222","areaCode":"023"}    "resultCode":"000001"

002_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

003_outOrderNo字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180030001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"orderNo":"11122233310","phonePay":"13618254716","packageCode":"000111222","areaCode":"023"}    "resultCode":"000001"

003_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

004_phonePay字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180040001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"orderNo":"11122233310","outOrderNo":"abcde123456","packageCode":"000111222","areaCode":"023"}    "resultCode":"000001"

004_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

005_packageCode字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180050001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"orderNo":"11122233310","outOrderNo":"abcde123456","phonePay":"13618254716","areaCode":"023"}    "resultCode":"000001"

005_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

006_areaCode字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180060001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {"orderNo":"11122233310","outOrderNo":"abcde123456","phonePay":"13618254716","packageCode":"000111222"}    "resultCode":"000001"

006_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0

007_请求载荷为空（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除待关联套餐}
    [Template]    HemuExecTestCases
    qos180060001    com.cmiot.qos.api.order.AddRevOrderService    addRevOrderService    {}    "resultCode":"000001"

007_确认待关联表未生成
    [Template]    hemu_query_db_result
    ${sql_确认生成待关联表}    0
