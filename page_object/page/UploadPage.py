import time

from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class UploadPage(BasePage):

    _color_loc = 'label == "联合 11"'  # 上色位置
    _apply_loc = 'label contains "Apply"'
    _cut_loc = 'label == "组 407"'  # 裁剪
    _cancle_cut = 'label == "组 408"'  # 撤销裁剪
    _rotate = 'label == "112233444"'  # 旋转
    _free_loc = 'label == "组 89"'  # free
    _one_loc = 'label == "组 93"'  # 1:1
    _three_loc = 'label == "组 95"'  # 3:2
    _four_loc = 'label == "组 99"'  # 4:3
    _sixteeth_loc = 'label == "组 101"'  # 16:9
    _go_home = 'label contains "Home"'  # 回到主页
    _take_pic = 'label == "Take a Photo"'  # 拍照位置
    _pic_capture = 'label == "Take Picture"'  # 拍照
    _user_pic = 'label == "Use Photo" AND name == "Use Photo" AND value == "Use Photo"'  # 应用图片
    _upload_pic = 'label contains "Upload a Photo"'  # 上传图片按钮
    _album_loc = "//*[contains(@type,'TypeCell')]"  # 相册列表

    def upload_pic(self, index):
        self.find_element_predicate(self._upload_pic).click()
    #     x = self.get_size()['width']
    #     y = self.get_size()['height']
    #     time.sleep(2)
    #     self.tap(x/3/2,(y-300)/4+(y-350)/2)
        ele = self.find_element_ablum(self._album_loc)
        ele[index].click()



    def colorize(self):
        self.find_element_predicate(self._color_loc).click()

    def edit_pic(self):
        self.find_element_predicate(self._cut_loc).click()
        self.find_element_predicate(self._free_loc).click()

    def cancel_edit(self):
        self.find_element_predicate(self._cut_loc).click()
        self.find_element_predicate(self._one_loc).click()
        self.find_element_predicate(self._three_loc).click()
        self.find_element_predicate(self._four_loc).click()
        self.find_element_predicate(self._sixteeth_loc).click()
        self.find_element_predicate(self._cancle_cut).click()

    def apply(self):
        self.find_element_predicate(self._apply_loc).click()

    def go_home(self):
        self.find_element_predicate(self._go_home).click()
        return MainPage()

    def take_pic(self):
        self.find_element_predicate(self._upload_pic).click()
        self.find_element_predicate(self._take_pic).click()
        self.find_element_predicate(self._pic_capture).click()
        self.find_element_predicate(self._user_pic).click()

    def ratate(self,index):
        for i in range(index):
            self.find_element_predicate(self._rotate).click()

