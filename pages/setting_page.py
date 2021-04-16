from peel_appiumTest.pages.basepage import BasePage
"""
    设置界面page层
"""
class SettingPage(BasePage):

    #   按钮 设置
    def button_setting(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_setting').click()
    #   按钮 账号管理
    def button_account_management(self):
        self.by_xpath('//*[@text="账号管理"]').click()

    """
        账号管理界面page层
    """
    #   按钮 账号管理
    def button_edit_password(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_manager_edit_password').click()
    """
        修改密码界面page层
    """
    #   输入框 密码
    def input_update_password(self,update_password):
        self.by_id('com.dongxiangtech.peeldiary:id/input_password').send_keys(update_password)
    #   输入框 验证码
    def input_update_code(self,update_code):
        self.by_id('com.dongxiangtech.peeldiary:id/input_code').send_keys(update_code)
    #   按钮 获取验证码
    def button_send(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_input_send').click()
    #   按钮 完成
    def button_submit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()



    #   按钮 微信绑定
    def button_weixin_bind(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_manager_we_chat').click()
    #   按钮 QQ绑定
    def button_qq_bind(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_manager_qq').click()
    #   按钮 账号注销
    def button_manager_logout(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_manager_logout').click()
    """
    账号注销界面page
    """
    #   输入框 注销原因
    def input_logoff_reason(self,logoff_reason):
        self.by_id('com.dongxiangtech.peeldiary:id/input_content').send_keys(logoff_reason)
    #   输入框 联系方式
    def input_logoff_phone(self,logoff_phone):
        self.by_id('com.dongxiangtech.peeldiary:id/input_address').send_keys(logoff_phone)
    #   按钮 提交
    def button_logoff_submit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   按钮 返回
    def button_logoff_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_tool_left').click()


    def button_feedback(self):
        self.by_xpath('//*[@text="意见反馈"]')
    """
        意见反馈界面page
    """
    #   输入框 意见
    def input_idea(self,idea):
        self.by_id('com.dongxiangtech.peeldiary:id/input_content').send_keys(idea)
    #   输入框 联系方式
    def input_idea_phone(self,idea_phone):
        self.by_id('com.dongxiangtech.peeldiary:id/input_address').send_keys(idea_phone)
    #   按钮 提交
    def button_idea_submit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   按钮 返回
    def button_idea_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_tool_left').click()


    def button_blacklist(self):
        self.by_xpath('//*[@text="黑名单"]')

    def button_about_us(self):
        self.by_xpath('//*[@text="关于我们"]')
    """
        关于我们界面page
    """
    #   按钮 用户注册协议
    def button_user_agreement(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_user_agreement').click()
    #   按钮 隐私协议
    def button_privacy_policy(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_privacy_policy').click()


    def button_logout(self):
        self.by_xpath('//*[@text="退出登陆"]')
    """
        退出登陆弹窗page
    """
    #   按钮 确定
    def button_pop_define(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_left').click()
    #   按钮 取消
    def button_pop_cancel(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_right').click()

    def webdriverwait_account(self):
        self.webdriverwait_byxpath('//*[@text="账号管理"]')

    def webdriverwait_bind(self):
        self.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_manager_we_chat')

