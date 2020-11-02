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
001_用户有待关联套餐（正）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    uom
    [Setup]
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    uom170010001    com.cmiot.uom.service.order.hoa.GetRevOrderService    invoke    {}    "resultCode":"000000"|"orderId":"10664729"|"itemCode":"sjkj_hka2"    mock_uom170010001    mock_uom170010002
    ...    mock_uom170010003    mock_uom170010004    mock_uom170010005    mock_uom170010006

002_用户没有待关联套餐（反）
    [Documentation]    测试用例报文结构：
    ...    第一列（必填）：测试用例编号。格式：模块号 + suiteId +caseId + 用例标签(例如：qos010010001)
    ...    第二列（必填）：测试接口url
    ...    第三列（必填）：测试接口方法
    ...    第四列（必填）：请求报文的载荷
    ...    第五列（必填）：预期结果（预期结果包含在实际测试结果中表示测试通过）
    ...    第六列，第七列 ...（非必填）：测试接口执行过程需要依赖的其它接口依次返回的响应，如果不需要依赖则不填。
    ...    例如：第六列填mock_1,第七列填mock_2则表示，该接口调用过程中需要按顺序依赖其它模块接口的返回，返回值分别为mock_1,mock_2。
    ...    Note：必须按照顺序依赖接口的调用顺序来依次填写
    [Tags]    uom
    [Setup]
    [Template]    HemuExecTestCases
    [Timeout]    20 seconds
    uom170020001    com.cmiot.uom.service.order.hoa.GetRevOrderService    invoke    {}    "resultCode":"000000"    mock_uom170010001    mock_uom170010002
    ...    mock_uom170020003
