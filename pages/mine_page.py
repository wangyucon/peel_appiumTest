from peel_appiumTest.pages.basepage import BasePage
"""
    我的界面page层
"""
class MinePage(BasePage):
    #   按钮 我的
    def button_mine(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_tab_mine').click()
    #   按钮 头像
    def button_user_head(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_mine_user_head').click()
    """
        更换头像界面page层
    """
    #   按钮 更换头像
    def button_edit_user_head(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   按钮 选择第一张图片
    def button_first_photo(self):
        self.by_id('com.dongxiangtech.peeldiary:id/media_item').click()
    #   按钮 图片剪裁完成
    def button_finish_user_head(self):
        self.by_id('com.dongxiangtech.peeldiary:id/done').click()
    #   按钮 关闭图片
    def button_image_close(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_image_close').click()

    #   按钮 编辑资料
    def button_info(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_edit_info').click()
    """
        编辑资料界面page层
    """
    #   按钮 昵称修改
    def button_edit_user_nickname(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_user_nickname').click()
    #   输入框 昵称
    def input_user_nickname(self,nickname):
        self.by_id('com.dongxiangtech.peeldiary:id/input_nickname').send_keys(nickname)
    #   按钮 确定
    def button_define(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_tool_right').click()
    #   按钮 签名
    def button_user_sign(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_user_sign').click()
    #   输入框 签名
    def input_user_sign(self,sign):
        self.by_id('com.dongxiangtech.peeldiary:id/input_sign').send_keys(sign)
    #   按钮 性别
    def button_user_sex(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_user_gender').click()
    #   按钮 性别-男
    def button_sex_boy(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_title').click()
    #   按钮 性别-女
    def button_sex_girl(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_cancel').click()
    #   按钮 城市
    def button_user_city(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_user_city').click()
    #   按钮 北京
    def button_user_city_bj(self):
        self.by_xpath('//*[@text="北京市"]').click()


    #   按钮 点赞
    def button_user_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_like').click()
    #   按钮 关注
    def button_user_follow(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_follow').click()
    #   按钮 粉丝
    def button_user_fans(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_mine_user_fans').click()
    #   按钮 动态
    def button_tab_life(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_tab_life').click()
    #   按钮 喜欢
    def button_tab_like(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_mine_tab_like').click()
    #   按钮 发布作品（当用户没有作品时显示<发布作品>按钮）
    def button_message(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_empty_message').click()

    def webdriverwait_mine(self):
        self.webdriverwait_byid('com.dongxiangtech.peeldiary:id/tv_tab_mine')
