#!/usr/bin/bash
TEST_MODULE=$1
SUITE_NAME=_suite
REPORT_NAME=_report
TEST_SUITE=$TEST_MODULE$SUITE_NAME
current_path=`pwd`
TEST_REPORT_DIR=$current_path/report/$TEST_MODULE$REPORT_NAME
SUPPORT_MODULE="ams bas cas cms dcs ddc dms lms mms mss oms pms qos sns sys syn ubs ugs ums uom uts vas"
echo "================================================================================================================"
if [ ! "`whoami`" == "iotest" ]
then
    echo "Please use the iotest user to install"
    exit 1
fi

#判断是否传入被测模块名称，传入则找出对应的配置文件名称
if [ ! -n "$1" ];then
  echo "No parameter,you should enter the test module name ..."
  echo "such as the format:./runtest.sh qos "
  echo "you can entered details for more detail ..."
  exit 1
elif [ "$1" = "details" ];then
  echo "you should enter the test module name as parameter to run the script..."
  echo "such as the format:./runtest.sh qos "
  echo "The test modules this platform support :"
  echo ${SUPPORT_MODULE[@]}
  exit 1
elif [[ "$SUPPORT_MODULE" =~ "$TEST_MODULE" ]];then
  echo "Parameter entered right ..."
  echo "Begin update the tdm ..."
else
  echo "Parameter wrong ..."
  echo "please enter commond : ./runtest.sh details  for more details"
  exit 1
fi

#判断测试报告存放目录是否存在
if [ ! -d $TEST_REPORT_DIR  ];then
  mkdir $TEST_REPORT_DIR
else
  echo "dir $TEST_REPORT_DIR exist"
fi
#python3 -m robot --outputdir $TEST_REPORT_DIR $current_path/$TEST_SUITE/01_QueryActOrdByDevService.robot
python3 -m robot --outputdir $TEST_REPORT_DIR $current_path/$TEST_SUITE/
