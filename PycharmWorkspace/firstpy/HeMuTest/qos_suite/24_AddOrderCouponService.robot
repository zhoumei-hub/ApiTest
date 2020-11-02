*** Settings ***
Resource          sql_values.txt
Resource          redis_values.txt
Resource          ../Common_config/config_data.txt
Resource          ../Common_lib/db_operation_lib.txt
Resource          ../Common_lib/redis_operation_lib.txt
Resource          ../Common_lib/robot_operation_lib.txt
Resource          ../Common_driver/test_case_driver.txt

*** Test Cases ***
001_成功生成可用优惠券（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240010001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000000"

001_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

002_orderSerialNumber字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240020001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

002_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

003_useCouponNumber字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240030001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

003_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

004_couponCode字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240040001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponName":"mytest","couponType":"2","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

004_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

005_couponName字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240050001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponType":"2","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

005_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

006_couponType字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240060001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponMinusCash":"","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

006_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

007_couponMinusCash字段可缺失（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240070001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","couponDiscount":"0.01","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000000"

007_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

008_couponDiscount字段可缺失（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240080001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000000"

008_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

009_phoneNumber字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240080001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","userId":"19926359","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

009_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

010_userId字段可缺失（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240100001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","devSn":"2059a0caa3d9","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000000"

010_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

011_devSn字段可缺失（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240110001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000000"

011_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

012_productPrice字段可缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240120001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","packageCode":"nmm_7_year_1","discountAmount":"11682","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

012_无可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

013_discountAmount字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240130001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","packageCode":"nmm_7_year_1","productPrice":"11800","payAmount":"118","usingStatus":"0"}    "resultCode":"000001"

013_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

014_payAmount字段缺失（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240140001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","usingStatus":"0"}    "resultCode":"000001"

014_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    0

015_usingStatus字段可缺失（正）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240150001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {"orderSerialNumber":"2019071515242904358999","useCouponNumber":"022240541519071582147999","couponCode":"022240541519071582147690","couponName":"mytest","couponType":"2","phoneNumber":"13618254716","packageCode":"nmm_7_year_1","productPrice":"11800","discountAmount":"11682","payAmount":"118"}    "resultCode":"000000"

015_确认可用优惠券生成
    [Template]    hemu_query_db_result
    ${sql_确认生成可用优惠券}    1

016_请求载荷payload为空（反）
    [Setup]    hemu_exec_commit_one_sql    ${sql_删除可用优惠券}
    [Template]    HemuExecTestCases
    qos240160001    com.cmiot.qos.api.order.AddOrderCouponService    addOrderCouponService    {}    "data":null
