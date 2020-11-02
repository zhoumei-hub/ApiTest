*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询出激活订单（正）
    [Setup]    hemu_exec_commit_four_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    qos130010001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "orderList":[{"id":100000441381

002_成功查询出待支付临时订单（正）
    [Setup]    hemu_exec_commit_four_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增待支付临时订单}
    [Template]    HemuExecTestCases
    qos130020001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "tempOrders":[{"id":18418461

003_成功查询预约续订套餐（正）
    [Setup]    hemu_exec_commit_four_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130030001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "appointOrderList":[{"id":300

004_成功全部套餐（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130040001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "orderList":[{"id":100000441381
    qos130040001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "tempOrders":[{"id":18418461
    qos130040001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "appointOrderList":[{"id":300

005_phone为空（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130050001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "appointOrderList":[{"id"

006_allDevSns为空（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130060001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":[""],"paymentWay":null,"appointStatus":[1]}    "appointOrderList":[{"id"

007_phone和allDevSns为空（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130070001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"","tempStatus":[2],"allDevSns":[""],"paymentWay":null,"appointStatus":[1]}    "appointOrderList":[],"orderList":[],"tempOrders":[]

008_appointStatus为空（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130080001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[]}    "resultCode":"000001"

009_tempStatus为空（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130090001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[]}    "resultCode":"000001"

010_缺少phone字段（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130100001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"tempStatus":[2],"allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "resultCode":"000001"

011_缺少allDevSns字段（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130110001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"paymentWay":null,"appointStatus":[1]}    "orderList":[{"id":100000441381

012_缺少tempStatus字段（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130120001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","allDevSns":["2059a0caa3d9"],"paymentWay":null,"appointStatus":[1]}    "orderList":[{"id":100000441381

013_缺少paymentWay字段（正）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130130001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["2059a0caa3d9"],"appointStatus":[1]}    "orderList":[{"id":100000441381

014_请求payload为空（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130140001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {}    "resultCode":"000000"

015_请求payload为空（反）
    [Setup]    hemu_exec_commit_six_sql    ${sql_删除已激活订单}    ${sql_删除待支付临时订单}    ${sql_删除待处理预约订单}    ${sql_新增已激活订单}    ${sql_新增待支付临时订单}
    ...    ${sql_新增待处理预约订单}
    [Template]    HemuExecTestCases
    qos130150001    com.cmiot.qos.api.order.QueryAllOrderService    invoke    {"phone":"13618254716","tempStatus":[2],"allDevSns":["aaabbbccc"],"appointStatus":[1]}    "orderList":[{"id":100000441381
