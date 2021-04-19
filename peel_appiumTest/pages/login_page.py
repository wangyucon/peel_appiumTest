from peel_appiumTest.peel_appiumTest.pages.basepage import BasePage
"""
    登陆界面page层
"""

class LogIn(BasePage):
    #   输入框 手机号码
    def input_phone(self,phone):
        self.by_id('com.dongxiangtech.peeldiary:id/input_phone').send_keys(phone)
    #   输入框 密码
    def input_password(self,password):
        self.by_id('com.dongxiangtech.peeldiary:id/input_password').send_keys(password)
    #   输入框 验证码
    def input_code(self,code):
        self.by_id('com.dongxiangtech.peeldiary:id/input_code').send_keys(code)
    #   按钮 获取验证码
    def button_code(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_input_send').click()
    #   按钮 登陆
    def button_login(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   按钮 微信授权
    def button_weixin(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_login_type_we_chat').click()
    #   按钮 qq授权
    def button_qq(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_login_type_qq').click()
    #   按钮 密码登陆
    def button_login_change(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_login_change').click()
    def webdriverwait_change(self):
       self.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_login_change')




