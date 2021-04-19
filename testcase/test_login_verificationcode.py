import pytest
from selenium.common.exceptions import TimeoutException
from ..pages import mine_page,login_page

class TestLogInVerificationCode():

    @pytest.mark.parametrize('phone',[(1761228224),(""),(17612282244)])
    def test_verificationcaode(self, init_peel, phone):
        lp = login_page.LogIn(init_peel)
        mp = mine_page.MinePage(init_peel)
        try:
            mp.webdriverwait_mine()
            mp.button_mine()
        except TimeoutException:
            pass

        lp.input_phone(phone)
        lp.button_code()

        if phone == 17612282244:
            # 等待加载图形锁弹窗
            lp.webdriverwait_byxpath('//*[@text="向右拖动滑块填充拼图"]')
            assert '向右拖动滑块填充拼图' == lp.get_text_by_xpath('//*[@text="向右拖动滑块填充拼图"]')
        else:
            assert '验证码登录' == lp.get_text_by_id('com.dongxiangtech.peeldiary:id/tv_login_title')





