import time
import pytest
import allure
from page_object.page.App import App


class TestUpload(object):

    @classmethod
    def setup_class(cls):
        cls.uploadPage = App.main()

    def setup_method(self):
        self.upload_photo = self.uploadPage.one_click()
        # self.upload_photo = self.uploadPage.cartoon()

    @allure.feature('test upload photo')
    @allure.story('test edit picture')
    def test_edit_pic(self):
        with allure.step("点击上传图片按钮"):
            self.upload_photo.upload_pic()
        with allure.step("点击裁剪按钮，并点击自由裁剪按钮"):
            self.upload_photo.edit_pic()
        with allure.step("点击应用图片"):
            self.upload_photo.apply()
        with allure.step("断言弹窗中是否有Uploading"):
            assert self.upload_photo.is_element_exist('Uploading')
        with allure.step("点击home，回到主页"):
            self.upload_photo.go_home()

    @allure.feature('test upload photo')
    @allure.story('test edit picture')
    def test_cancel_edit(self):
        self.upload_photo.upload_pic()
        self.upload_photo.cancel_edit()
        self.upload_photo.apply()
        assert self.upload_photo.is_element_exist('Uploading')
        self.upload_photo.go_home()

    @allure.feature('test upload photo')
    @allure.story('test rotate picture')
    @pytest.mark.parametrize("index",(2,))
    def test_rotate(self,index):
        self.upload_photo.upload_pic()
        self.upload_photo.ratate(index)
        self.upload_photo.apply()
        assert self.upload_photo.is_element_exist('Uploading')
        self.upload_photo.go_home()

    @allure.feature('test upload photo')
    @allure.story('test colorize picture')
    def test_colorize(self):
        with allure.step("点击上传图片按钮"):
            self.upload_photo.upload_pic()
        with allure.step("点击上色按钮"):
            self.upload_photo.colorize()
        with allure.step("点击应用图片按钮"):
            self.upload_photo.apply()
        with allure.step("设置等待20秒"):
            time.sleep(20)
        with allure.step("设置断言，返回是否有Video字样"):
            assert self.upload_photo.is_element_exist('Video')
        with allure.step("点击返回按钮，返回应用图片页面"):
            self.upload_photo.back()
        with allure.step("点击返回按钮，返回选择照片或者拍照页面"):
            self.upload_photo.back()
        with allure.step("点击返回按钮，返回上传图片按钮页面"):
            self.upload_photo.back()
        with allure.step("点击返回按钮，回到主页"):
            self.upload_photo.back()

    @allure.feature('test upload photo')
    @allure.story('test take a photo')
    @pytest.mark.ios
    def test_take_pic(self):
        with allure.step("点击拍照按钮"):
            self.upload_photo.take_pic()
        with allure.step("点击应用图片按钮"):
            self.upload_photo.apply()
        with allure.step("等待20秒"):
            time.sleep(20)
        with allure.step("断言是否存在Video字样"):
            assert self.upload_photo.is_element_exist('Photo')
