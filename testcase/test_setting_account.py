from peel_appiumTest.pages import setting_page
from peel_appiumTest.testcase import test_login_success

class TestSettingAccount():

    def test_account_bind(self,init_peel):
        sp = setting_page.SettingPage(init_peel)
        tls = test_login_success.TestLogInSuccess()

        tls.test_login_success(init_peel,17612282244,123456)

        sp.button_setting()

        sp.webdriverwait_byxpath('//*[@text="账号管理"]')
        sp.button_account_management()

        sp.webdriverwait_bind()
        sp.button_weixin_bind()
        print(sp.get_toast('你已经绑定微信了'))
        assert '你已经绑定微信了' == sp.get_toast('你已经绑定微信了')

        sp.button_qq_bind()
        assert '你已经绑定QQ了' == sp.get_toast('你已经绑定QQ了')

    def test_account_password(self,init_peel):
        sp = setting_page.SettingPage(init_peel)

        sp.button_edit_password()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/btn_submit')
        sp.input_update_password('123456')
        sp.button_send()
        sp.webdriverwait_byxpath('//*[@text="向右拖动滑块填充拼图"]')
        assert '向右拖动滑块填充拼图' == sp.get_text_by_xpath('//*[@text="向右拖动滑块填充拼图"]')
