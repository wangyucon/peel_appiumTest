from peel_appiumTest.peel_appiumTest.pages.basepage import BasePage
"""
    话题界面page层
"""
class Topicpage(BasePage):
    #   按钮 话题
    def button_topic(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_tab_topic').click()
    #   按钮 推荐
    def button_topic_recommend(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_topic_tab_recommend').click()
    #   按钮 最新
    def button_topic_new(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_topic_tab_new').click()
    #   按钮 参与话题
    def button_topic_join(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_topic_public').click()