from peel_appiumTest.pages.basepage import BasePage
"""
    公共界面page层
"""

class PublicPage(BasePage):
    #   按钮 取消
    def button_cancel(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_cancel').click()
    #   按钮 退出
    def button_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_tool_left').click()
