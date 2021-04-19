from peel_appiumTest.peel_appiumTest.pages.basepage import BasePage
"""
    0元抽奖界面page层
"""
class LotteryDrawPage(BasePage):
    #   按钮 0元抽奖占位图
    def button_lottery_draw(self):
        self.by_xpath('//android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView').click()
    #   按钮 往期抽奖
    def button_draw_history(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_history').click()
    #   按钮 抽奖规则
    def button_lottery_rule(self):
        self.by_xpath('//*[@text="抽奖规则"]').click()
    #   按钮 0元参与抽奖/任务列表
    def button_join(self):
        self.by_id('com.dongxiangtech.peeldiary:id/view_button').click()

    #   按钮 活动（第二个活动，第一个进行中活动，第一个活动为已结束活动）
    def button_activity(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView').click()
    #   按钮 弹窗完成任务
    def button_pop_finish(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_dialog_next').click()
    #   按钮 分享
    def button_draw_share(self):
        self.by_xpath('//*[@text="分享"]').click()
    """
    分享弹窗page
    """
    #   按钮 QQ好友
    def button_draw_qq(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
    #   按钮 QQ空间
    def button_draw_qqspace(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    #   按钮 微信
    def button_draw_weixin(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()
    #   按钮 微信朋友圈
    def button_draw_wxspace(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]').click()


    #   按钮 邀请
    def button_draw_invite(self):
        self.by_xpath('//android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.TextView').click()
    #   按钮 创作
    def button_draw_create(self):
        self.by_xpath('//*[@text="创作"]').click()
    #   按钮 点赞
    def button_draw_like(self):
        self.by_xpath('//*[@text="点赞"]').click()


