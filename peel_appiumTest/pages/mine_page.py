from peel_appiumTest.peel_appiumTest.pages.basepage import BasePage
"""
    我的界面page层
"""
class MinePage(BasePage):
    #   按钮 我的
    def button_mine(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_tab_mine').click()
    #   按钮 头像
    def button_user_head(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_mine_user_head').click()
    #   按钮 编辑资料
    def button_info(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_edit_info').click()
    #   按钮 点赞
    def button_user_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_like').click()
    #   按钮 关注
    def button_user_follow(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_follow').click()
    #   按钮 粉丝
    def button_user_fans(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_fans').click()
    #   按钮 动态
    def button_tab_life(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_tab_life').click()
    #   按钮 喜欢
    def button_tab_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_tab_like').click()
    #   按钮 发布作品（当用户没有作品时显示<发布作品>按钮）
    def button_message(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_empty_message').click()

    def webdriverwait_mine(self):
        self.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_tab_mine')
