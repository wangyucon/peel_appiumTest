import pytest
import os
from py.xml import html
from appium import webdriver
from config import RunConfig

# 项目报告目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/testreport/"

@pytest.fixture(scope='class')
def init_peel():

    global driver
    desired_caps = {}
    desired_caps['platformName'] = RunConfig.platformName
    desired_caps['platformVersion'] = RunConfig.platformVersion
    desired_caps['deviceName'] = RunConfig.deviceName
    desired_caps['appPackage'] = RunConfig.appPackage
    desired_caps['appActivity'] = RunConfig.appActivity
    desired_caps['automationName'] = RunConfig.automationName
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    RunConfig.driver = driver

    yield driver

    driver.quit()
    print("test end!")

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = description_html(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             case_path = report.nodeid.replace("::", "_") + ".png"
#             print("case_path : "+case_path)
#             if "[" in case_path:
#                 case_name = case_path.split("-")[0] + "].png"
#             else:
#                 case_name = case_path
#             capture_screenshots(case_name)
#             img_path = "image/" + case_name.split("/")[-1]
#             print("img_path : "+img_path)
#             if img_path:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % img_path
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def capture_screenshots(case_name):
#     """
#     配置用例失败截图路径
#     :param case_name: 用例名
#     :return:
#     """
#     global driver
#     file_name = case_name.split("/")[-1]
#     print(RunConfig.NEW_REPORT)
#     print("###################")
#     if RunConfig.NEW_REPORT is None:
#         raise NameError('没有初始化测试报告目录')
#     else:
#         image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
#         print("image_dir : " +image_dir)
#         RunConfig.driver.save_screenshot(image_dir)
#
#
# def description_html(desc):
#     """
#     将用例中的描述转成HTML对象
#     :param desc: 描述
#     :return:
#     """
#     if desc is None:
#         return "No case description"
#     desc_ = ""
#     for i in range(len(desc)):
#         if i == 0:
#             pass
#         elif desc[i] == '\n':
#             desc_ = desc_ + ";"
#         else:
#             desc_ = desc_ + desc[i]
#
#     desc_lines = desc_.split(";")
#     desc_html = html.html(
#         html.head(
#             html.meta(name="Content-Type", value="text/html; charset=latin1")),
#         html.body(
#             [html.p(line) for line in desc_lines]))
#     return desc_html