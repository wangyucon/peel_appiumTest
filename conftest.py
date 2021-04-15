import pytest
import os
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
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    RunConfig.driver = driver

    yield driver

    driver.quit()
    print("test end!")