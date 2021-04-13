import pytest

from appium import webdriver


@pytest.fixture(scope='class')
def init_peel():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # 真机系统版本
    # desired_caps['platformVersion'] = '10'
    desired_caps['platformVersion'] = '7'
    desired_caps['deviceName'] = 'HONOR 20 Lite'
    desired_caps['appPackage'] = 'com.dongxiangtech.peeldiary'
    # 真机启动Activity
    desired_caps['appActivity'] = '.main.MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    yield driver
    driver.quit()