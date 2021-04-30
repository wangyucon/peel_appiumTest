from peel_appiumTest.pages import setting_page,public_page
from peel_appiumTest.testcase import test_login_success

class TestSettingAccount():
    def test_feedback(self,init_peel):
        sp = setting_page.SettingPage(init_peel)
        tls = test_login_success.TestLogInSuccess()

        tls.test_login_success(init_peel, 17612282244, 123456)
        sp.button_setting()

        sp.webdriverwait_byxpath('//*[@text="账号管理"]')
        sp.button_feedback()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/btn_submit')
        # 不填写意见直接点击<提交>按钮
        sp.button_submit()
        sp.get_toast('请填写你要反馈的信息！')
        # 填写意见和联系方式点击<提交>按钮
        sp.input_idea('意见反馈自动化测试')
        sp.input_idea_phone(17612882244)
        sp.button_submit()
        sp.get_toast('提交成功')

    def test_logout(self,init_peel):
        sp = setting_page.SettingPage(init_peel)
        pp = public_page.PublicPage(init_peel)
        sp.button_setting()

        sp.webdriverwait_byxpath('//*[@text="账号管理"]')
        sp.button_about_us()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_user_agreement')
        sp.button_user_agreement()
        sp.webdriverwait_byxpath('//*[@text="用户注册协议"]')
        sp.button_close()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_user_agreement')
        sp.button_privacy_policy()
        sp.webdriverwait_byxpath('//*[@text="隐私政策"]')
        sp.button_close()
        pp.button_exit()

        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/ll_mine_setting')
        sp.button_setting()

        sp.webdriverwait_byxpath('//*[@text="账号管理"]')
        sp.button_logout()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_dialog_left')
        sp.button_pop_define()
        sp.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_login_title')
        login_title = sp.get_text_by_id('com.dongxiangtech.peeldiary:id/tv_login_title')
        assert login_title == "验证码登录"

