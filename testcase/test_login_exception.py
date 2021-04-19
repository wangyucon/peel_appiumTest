"""
手机号密码登陆异常用例集合
对手机号密码输入框使用非法参数进行入参
点击登录按钮后断言非法输入登录后仍停留在当前界面
"""
import pytest
from selenium.common.exceptions import NoSuchElementException
from peel_appiumTest.pages import login_page, mine_page


class TestLogInException():
    # 用例参数化
    @pytest.mark.parametrize('phone,password',[(1761228224,123456),(17612282244,12345),
                                    ('',123456),(17612282244,''),(17612282244,1234567),('','')])
    def test_login_exception(self,init_peel,phone,password):
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

        text = lp.get_text_by_id('com.dongxiangtech.peeldiary:id/tv_login_title')
        assert text == '密码登录'
