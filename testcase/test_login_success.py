"""
手机号密码登陆
对手机号密码输入框使用已存在账号进行登陆
通过断言 我的——昵称 判断是否登陆成功
"""
import pytest
from selenium.common.exceptions import NoSuchElementException
from peel_appiumTest.pages import login_page,mine_page

class TestLogInSuccess():
    @pytest.mark.parametrize('phone,password', [(17612282244, 123456)])
    def test_login_long_fail(self, init_peel, phone, password):
        # 实例化page对象
        lp = login_page.LogIn(init_peel)
        mp = mine_page.MinePage(init_peel)

        try:
            mp.button_mine()
            lp.webdriverwait_change()
            lp.button_login_change()
        except NoSuchElementException:
            pass

        lp.input_phone(phone)
        lp.input_password(password)
        lp.button_login()
        mp.button_mine()

        text = lp.get_text_by_xpath('//*[@text="等风"]')
        assert text == '等风'


