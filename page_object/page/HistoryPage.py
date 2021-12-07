import time

from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class HistoryPage(BasePage):

    _download = 'label == "组 125"'  # 下载按钮
    _share = 'label == "组 107"'  # 分享按钮
    _delete = 'label == "组 124"'  # 删除按钮
    _delete_sure = 'label == "Delete"'
    _before = 'label == "Before"'
    _after = 'label == "After"'
    _drag = '//*[@name="drag"]/..'  # 增强图片左右滑动位置
    # _repair_list = '//*[contains(@type,"TypeImage")]/../..'
    _repair_list = '//*[contains(@type,"CollectionView")]//*[contains(@type,"TypeCell")]'
    _delete_icon = 'label == " " AND name == " "'  # 下载后弹出的分享框的x按钮位置
    _shut_share = 'label Contains "remind me again"'  # 弹出框的"不再提醒我"位置
    _TW = 'label == "Twitter" and type contains "TypeButton"'   # twitter
    _FB = 'label == "Facebook" and type contains "TypeButton"'  # facebook
    _Ins = 'label == "Instagram" and type contains "TypeButton"'  # Instagram

    def open_pic(self, index):
        # x = self.get_size()['width']
        # y = self.get_size()['height']
        # self.tap(x / 3 / 2 + x / 3, 445)
        eles = self.find_element_ablum(self._repair_list)
        eles[index].click()

    def download_pic(self):
        self.find_element_predicate(self._download).click()

    def close_alert(self):   # 关闭下载弹出的分享弹窗
        self.find_element_predicate(self._delete_icon).click()

    def share(self):
        self.find_element_predicate(self._share).click()

    def fb(self):
        self.find_element_predicate(self._FB).click()

    def tw(self):
        self.find_element_predicate(self._TW).click()

    def ins(self):
        self.find_element_predicate(self._Ins).click()

    def delete_pic(self):
        self.find_element_predicate(self._delete).click()
        self.find_element_predicate(self._delete_sure).click()

    def swipe_screen(self, count):
        for i in range(count):
            self.swipe_up()

    def scroll(self):
        self.drag(self.find_element_xpath(self._drag), self.find_element_predicate(self._before))
        self.drag(self.find_element_xpath(self._drag), self.find_element_predicate(self._after))
