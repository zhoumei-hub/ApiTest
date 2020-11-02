*** Settings ***
Resource          ../sql_values.txt
Resource          ../redis_values.txt
Resource          ../../Common_config/config_data.txt
Resource          ../../Common_lib/db_operation_lib.txt
Resource          ../../Common_lib/redis_operation_lib.txt
Resource          ../../Common_lib/robot_operation_lib.txt
Resource          ../../Common_driver/test_case_driver.txt
Library           ../../Common_lib/python_lib/python_operation_lib.py

*** Variables ***

*** Test Cases ***
001_新增1条点播类资费点信息（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200010001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "payCode": "30001185950001", \ "payName": "test", "feeType": "1", \ "price": "100","description": "123" }    "resultCode":"000000"

002_新增1条连续包月类资费点信息（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200020001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "payCode": "30001185950001", \ "payName": "test", "feeType": "2", \ "price": "100","description": "123" }    "resultCode":"000000"

003_新增资费点已存在（反）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}    ${sql_zm_新增资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200030001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "payCode": "30001185950001", \ "payName": "test", "feeType": "1", \ "price": "100","description": "123" }    "resultMsg":"已存在相同资费编码"

004_新增资费点paycode字段非空校验（反）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200040001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    {"payName": "test", "feeType": "2", \ "price": "100","description": "123" }    "resultMsg":"资费编码不能为空"

005_新增资费点paytype字段非空校验（反）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200050001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "payCode": "30001185950001", \ "payName": "test","price": "100","description": "123" }    "resultMsg":"资费类型不能为空"

006_修改资费点名称（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}    ${sql_zm_新增资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200060001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "id":"140","payCode": "30001185950001", "payName": "test1", "feeType": "1", "price": "100","description": "123" }    "resultCode":"000000"

007_修改资费点价格（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}    ${sql_zm_新增资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200080001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "id":"140","payCode": "30001185950001", "payName": "test1", "feeType": "1", "price": "101","description": "123" }     "resultCode":"000000"

008_修改资费点描述（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    pms
    [Setup]    hemu_exec_commit_sql    ${sql_zm_删除资费点信息}    ${sql_zm_新增资费点信息}
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    pms200080001    com.cmiot.pms.api.iotmm.AddOrUpdateIotmmPayCodeInfo    invoke    { "id":"140","payCode": "30001185950001", "payName": "test1", "feeType": "1", "price": "100","description": "321" }     "resultCode":"000000"
