*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功返回失效套餐（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030010001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"10","page":"1","allDevSns":["2059a0caa3d9","cde010000001"]}    "phonePay":"13618254716"

002_pageSize允许为空（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030020001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","page":"1","allDevSns":["2059a0caa3d9","cde010000001"]}    "phonePay":"13618254716"

003_Page允许为空（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030030001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"10","allDevSns":["2059a0caa3d9","cde010000001"]}    "phonePay":"13618254716"

004_allDevSns允许为空（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030040001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"10","page":"1"}    "phonePay":"13618254716"

005_只填电话号码（正）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030050001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716"}    "phonePay":"13618254716"

006_电话号码不在系统中（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030060001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"136182547168","pageSize":"10","page":"1","allDevSns":["2059a0caa3d9","cde010000001"]}    "data":[]

007_电话号码字段为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030070001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"","pageSize":"10","page":"1","allDevSns":["2059a0caa3d9","cde010000001"]}    "resultCode":"000003"

008_请求报文为空（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030080001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {}    "resultCode":"000003"

009_请求报文pageSize类型错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030090001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"stringtest","page":"1","allDevSns":["2059a0caa3d9","cde010000001"]}    "resultCode":"000003"

010_请求报文page类型错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030100001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"10","page":"stringtest","allDevSns":["2059a0caa3d9","cde010000001"]}    "resultCode":"000003"

011_请求报文allDevSns类型错误（反）
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除失效订单}    ${sql_新增失效订单}
    [Template]    HemuExecTestCases
    qos030110001    com.cmiot.qos.api.order.QueryInvalidOrderService    invoke    {"phone":"13618254716","pageSize":"10","page":"1","allDevSns":"stringtest"}    "resultCode":"000003"
