from peel_appiumTest.peel_appiumTest.pages.basepage import BasePage
"""
    作品详情页page层
"""
class InvitationPage(BasePage):
    #   按钮 话题
    def button_invitation_topic(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_article_topic_title').click()
    #   按钮 关注
    def button_invitation_follow(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_detail_follow_state').click()
    #   按钮 更多
    def button_invitation_more(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_detail_more').click()
    #   按钮 评论
    def input_invitation_comment(self,comment):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_input_comment').send_keys(comment)
    #   按钮 点赞
    def button_invitation_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_comment_like').click()
    #   按钮 QQ分享
    def button_invitation_qq(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
    #   按钮 微信分享
    def button_invitation_wx(self):
        self.by_xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()
    #   按钮 作品举报
    def button_invitation_report(self):
        self.by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout').click()
    """
    作品举报界面page
    """
    #   按钮 作品举报类型（包括色情低俗、政治敏感、广告内容、搬运内容、不友善内容、其他）
    def button_report_type(self):
        self.by_xpath('//*[@text="政治敏感"]')
    #   输入框 举报理由
    def input_report_body(self,report_body):
        self.by_id('com.dongxiangtech.peeldiary:id/input_body').send_keys(report_body)
    #   按钮 图片添加
    def button_report_add(self):
        self.by_id('com.dongxiangtech.peeldiary:id/cv_image_add').click()
    #   按钮 提交举报
    def button_report_submit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   文字 举报类型
    def text_report_type(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_report_name').get_text()

