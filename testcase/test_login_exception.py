import pytest
from selenium.common.exceptions import NoSuchElementException
from peel_appiumTest.pages import login_page,mine_page

class TestLogInException():

    @pytest.mark.parametrize('phone,password',[(1761228224,123456),(17612282244,12345),
                                    ('',123456),(17612282244,''),('',''),(176122822444,123456),(17612282244,1234567)])
    @pytest.mark.run(order=1)
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

        text = lp.get_text_by_id('com.dongxiangtech.peeldiary:id/tv_login_title')
        assert text == '密码登录'
