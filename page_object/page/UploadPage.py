import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException

from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class UploadPage(BasePage):

    _color_loc = 'label contains "联合 11"'  # 上色位置
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
    _upload_pic = 'label contains "Choose"'  # 上传图片按钮
    _album_loc = '//*[contains(@type,"TypeCell")]'  # 相册列表
    _halloween_list = '//*[contains(@type,"TypeCell")]'  # 万圣节滤镜列表
    _halloween_loc = '//*[contains(@type,"CollectionView")]'  # 万圣节滤镜列表的层级元素，便于滑动点击后面的元素

    def upload_pic(self, index):
        self.find_element_predicate(self._upload_pic).click()
        self.accept_alert()
        try:
            ele = self.find_element_ablum(self._album_loc)
            ele[index].click()
        except StaleElementReferenceException as e:
            print(f'查找元素异常{e}')
            print('重新获取元素')
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
        self.accept_alert()
        self.find_element_predicate(self._pic_capture).click()
        self.find_element_predicate(self._user_pic).click()

    def rotate(self, index):
        for i in range(index):
            self.find_element_predicate(self._rotate).click()

    def halloween_choice(self, index):
        eles = self.find_element_ablum(self._halloween_list)
        time.sleep(2)
        if index < 5:
            eles[index].click()
        else:
            for i in range(1, index // 5 + 1):
                x = self.get_size()['width']
                y = self.get_size()['height']
                end_x = int((20 / 375) * x)
                start_y = int((620 / 812) * y)
                start_x = int((350 / 375) * x)
                # driver.swipe(350, 620, 20, 620, 1000)   # 测试机的坐标
                self.drag_left(start_x, start_y, end_x, start_y)
                time.sleep(5)
                eles = self.find_element_ablum(self._halloween_list)
                print(index - (5 * i))
                eles[index - (5 * i)].click()













