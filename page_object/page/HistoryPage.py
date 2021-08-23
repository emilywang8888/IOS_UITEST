import time

from page_object.page.BasePage import BasePage


class HistoryPage(BasePage):

    _download = 'label == "组 125"'  # 下载按钮
    _share = 'label == "组 107"'  # 分享按钮
    _delete = 'label == "组 124"'  # 删除按钮
    _delete_sure = 'labe contains "Delete"'

    def open_pic(self):
        x = self.get_size()[0]
        y = self.get_size()[1]
        self.tap(x / 3 / 2+100, y / 4 + y/4 / 2)

    def download_pic(self):
        self.find_element_predicate(self._download).click()

    def share(self):
        self.find_element_predicate(self._share).click()

    def delete_pic(self):
        self.find_element_predicate(self._delete).click()
        self.find_element_predicate(self._delete_sure).click()

    def swipe_screen(self,count):
        for i in range(count):
            self.swipe_up()
