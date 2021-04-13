from peel_appiumTest.pages.basepage import BasePage
"""
    消息界面page层
"""
class MessagePage(BasePage):
    #   按钮 消息
    def button_message(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_tab_msg').click()
    #   按钮 获赞列表
    def button_message_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_message_like_icon').click()
    #   按钮 获评论列表
    def button_message_comment(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_message_comment_icon').click()
    #   按钮 粉丝消息列表
    def button_message_fans(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_message_fans_icon').click()
    #   按钮 系统消息列表
    def button_message_system(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_msg_image').click()