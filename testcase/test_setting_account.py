from peel_appiumTest.pages import setting_page
import test_login_success

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
