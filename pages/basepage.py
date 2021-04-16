

from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self,driver):
        self.driver = driver
    """果皮page基层，果皮页面封装操作到的元素"""

    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_class(self,class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_xpath(self,xpth):
        return self.driver.find_element_by_xpath(xpth)

    #   获取元素text属性
    def get_text_by_xpath(self,xpath):
        return self.by_xpath(xpath).text

    def get_text_by_id(self,id_):
        return self.by_id(id_).text

    # 物理外键------------------------------------------------
    # 返回键4 HOME键3 音量增加键24 音量减少键25
    def keyevent(self,key):
        self.driver.keyevent(key)

    """
    Appium 显示等待
    By Id
    By Xpath
    """
    def webdriverwait_byid(self,id):
        wait = WebDriverWait(self.driver,5,0.2)
        wait.until(EC.presence_of_element_located((By.ID, id)))

    def webdriverwait_byxpath(self,xpath):
        wait = WebDriverWait(self.driver,5,0.2)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


    """
    Appium 屏幕页面滑动（swipe函数实现）
    """
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)
    def swipUp(self,t,n):
        l = BasePage.getSize(self)
        x1 = int(l[0] * 0.5) #x起始位置
        y1 = int(l[1] * 0.75) #y起始位置
        y2 = int(l[1] * 0.25) #y终点位置
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,t)
    def swipDown(self,t,n):
        l = BasePage.getSize(self)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,t)
    def swipLeft(self,t,n):
        l = BasePage.getSize(self)
        x1 = int(l[0] * 0.85) #x起始位置
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.15)
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,t)
    def swipRight(self,t,n):
        l = BasePage.getSize(self)
        x1 = int(l[0] * 0.15)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.85)
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,t)

    """
    自动化获取toast消息
    """
    def get_toast(self,toast):

        wait = WebDriverWait(self.driver, 10, 0.2)
        a = wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@text='+'"'+toast+'"'+']')))
        return a.text








