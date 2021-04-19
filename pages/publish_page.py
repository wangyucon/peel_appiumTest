from peel_appiumTest.pages.basepage import BasePage
"""
    发布界面page层
"""

class PublishPage(BasePage):
    #   按钮 发布
    def button_publish(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_public').click()
    #   按钮 下一步
    def button_publish_next(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_album_next').click()
    #   按钮 选择照片
    def button_publish_select(self):
        self.by_id('com.dongxiangtech.peeldiary:id/media_item_check').click()
    #   按钮 预览照片
    def button_publish_cpt(self):
        self.by_id('com.dongxiangtech.peeldiary:id/media_item').click()
    """
         预览界面page层
    """
    #   按钮 下一步
    def button_cpt_select(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_select_state').click()
    #   按钮 退出
    def button_cpt_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_close').click()



    #   按钮 退出
    def button_publish_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_media_close').click()
    #   按钮 相册
    def button_publish_photo(self):
        self.by_id('com.dongxiangtech.peeldiary:id/cl_media_album').click()
    #   按钮 拍照
    def button_publish_photograph(self):
        self.by_id('com.dongxiangtech.peeldiary:id/cl_media_photo').click()
    """
         拍照界面page层
    """
    #   按钮 拍照
    def button_capture(self):
        self.by_id('com.dongxiangtech.peeldiary:id/lsq_captureButton').click()

    """
        图片编辑界面page层
    """
    #   按钮 裁剪
    def button_edit_toilor(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_image_crop').click()
    #   按钮 退出
    def button_edit_exit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_media_close').click()
    #   按钮 滤镜
    def button_edit_filter(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_image_filter').click()
    #   按钮 下一步
    def button_edit_next(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_image_next').click()

    """
         作品编辑界面page层
    """
    #   输入框 作品标题
    def input_publish_title(self,title):
        self.by_id('com.dongxiangtech.peeldiary:id/input_public_title').send_keys(title)
    #   输入框 作品正文
    def input_publish_body(self,body):
        self.by_id('com.dongxiangtech.peeldiary:id/input_public_body').send_keys(body)
    #   按钮 退出
    def button_topic_select(self):
        self.by_id('com.dongxiangtech.peeldiary:id/ll_public_topic').click()
    #   按钮 发布
    def button_publish_submit(self):
        self.by_id('com.dongxiangtech.peeldiary:id/btn_submit').click()
    #   按钮 添加图片
    def button_publish_addimage(self):
        self.by_id('com.dongxiangtech.peeldiary:id/cv_image_add').click()
    #   按钮 图片
    def button_publish_picture(self):
        self.by_id('com.dongxiangtech.peeldiary:id/iv_image').click()
    #   按钮 删除照片
    def button_delete_image(self):
        self.by_id('com.dongxiangtech.peeldiary:id/tv_dialog_title').click()








