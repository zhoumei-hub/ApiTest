*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功查询到一个设备的激活套餐（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    qos
    [Setup]    hemu_exec_commit_two_sql    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020010001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    13618254716|"deviceMac":"2059a0caa3d9"    mock_template_010101    mock_template_010102
    [Teardown]    hemu_exec_commit_one_sql    ${sql_删除运行记录}

002_成功查询多个设备的激活套餐（正）
    [Tags]    qos
    [Setup]    hemu_exec_commit_four_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}    ${sql_新增已激活订单1}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020020001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    13618254716    mock_template_010101    mock_template_010102

003_查询请求userid不在系统中（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020030001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"111222333aa"}    "data":[]    mock_template_010204    mock_template_010205

004_查询请求userid为空（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020040001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":""}    "resultCode":"000003"

005_查询请求payload为空（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020050001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"":""}    "resultCode":"000003"

006_mock查询电话号码返回格式错误（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020060001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    "resultCode":"000001"    mock_template_010206

007_mock查询mac返回格式错误（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020070001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    "resultCode":"000001"    mock_template_010101    mock_template_010207

008_mock查询电话号码不返回（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020080001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    "resultCode":"000001"

009_mock查询mac不返回（反）
    [Tags]    qos
    [Setup]    hemu_exec_commit_three_sql    ${sql_删除运行记录}    ${sql_删除已激活订单}    ${sql_新增已激活订单}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    qos020010001    com.cmiot.qos.api.QueryActiveOrder    invoke    {"userId":"19926359"}    "resultCode":"000001"    mock_template_010101
