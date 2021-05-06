from peel_appiumTest.pages import mine_page
from peel_appiumTest.testcase import test_login_success

class TestEditProfile():

    def test_edit_head(self,init_peel):
        mp = mine_page.MinePage(init_peel)
        tls = test_login_success.TestLogInSuccess()

        tls.test_login_success(init_peel, 17612282244, 123456)
        mp.button_user_head()
        # 点击用户头像，更改用户头像
        mp.button_user_head()
        mp.webdriverwait_byxpath('更换头像')
        mp.button_edit_user_head()
        mp.webdriverwait_byxpath('所有图片')
        mp.button_first_photo()
        mp.webdriverwait_byxpath('图片剪裁')
        mp.button_finish_user_head()
        mp.get_toast('编辑成功')
        mp.button_image_close()

    def test_edit_profile(self,init_peel):
        mp = mine_page.MinePage(init_peel)

        mp.button_info()
        mp.webdriverwait_byxpath('编辑资料')
        # 修改昵称
        mp.button_edit_user_nickname()
        mp.webdriverwait_byxpath('修改昵称')
        mp.input_user_nickname('等风')
        mp.button_define()
        mp.get_toast('编辑成功')
        # 修改简介
        mp.button_user_sign()
        mp.webdriverwait_byxpath('修改简介')
        mp.input_user_sign('-')
        mp.button_define()
        mp.get_toast('编辑成功')
        # 修改性别
        mp.button_user_sex()
        mp.webdriverwait_byxpath('男')
        mp.button_sex_boy()
        mp.get_toast('编辑成功')
        # 修改城市
        mp.button_user_city()
        mp.webdriverwait_byxpath('设置地区')
        mp.button_user_city_bj()
        mp.get_toast('编辑成功')

