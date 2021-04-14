import os
import time

import pytest
now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
print(now_time)
html_report = os.path.join("testreport",now_time,"report.html")
xml_report = os.path.join("testreport",now_time,"junit-xml.xml")

if __name__ =="__main__":
    print("测试已完成...等待输出测试报告")
    pytest.main(["testcase/","-s",
                 "--html=" + html_report,
                "--junit-xml=" + xml_report])