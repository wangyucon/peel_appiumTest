import os

PRO_PATH = os.path.dirname(os.path.abspath(__file__))

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录
    case_path = os.path.join(PRO_PATH, 'testcase')

    # 平台名称
    platformName = 'Android'

    # 平台版本
    platformVersion = '7'

    # 设备名称
    deviceName = 'HONOR 20 Lite'

    # 果皮日记包名
    appPackage = 'com.dongxiangtech.peeldiary'

    # 果皮日记首页Activity
    appActivity = '.main.MainActivity'

    # 真机驱动（不需要修改）
    driver = None

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 报告路径（不需要修改）
    NEW_REPORT = None

    automationName = 'UiAutomator2'