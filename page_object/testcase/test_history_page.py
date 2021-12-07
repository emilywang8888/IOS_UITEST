import time
import allure
import pytest
from pytest_assume.plugin import assume

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestHistory(object):

    @classmethod
    def setup_class(cls):
        cls.historyPage = App.main()

    def setup_method(self):
        self.history = self.historyPage.goto_history()
        time.sleep(10)

    @allure.feature('test history page')
    @allure.story('test download photo')
    def test_download(self):
        self.history.open_pic(1)
        time.sleep(2)
        self.history.download_pic()
        time.sleep(1)
        assert self.history.is_element_exist('Image saved successfully')
        self.history.close_alert()
        self.history.back()

    @allure.feature('test history page')
    @allure.story('scroll enhance photo')
    def test_scroll(self):
        self.history.open_pic(1)
        time.sleep(2)
        if self.history.is_element_exist('enhance'):
            for i in range(5):
                self.history.scroll()
        assert self.history.is_element_exist('After')
        self.history.back()

    @allure.feature('test history page')
    @allure.story('test swipe up')
    @pytest.mark.parametrize("n", (5,))
    def test_swipe(self, n):
        self.history.swipe_screen(n)

    @allure.feature('test history page')
    @allure.story('test delete photo')
    def test_del(self):
        self.history.open_pic(0)
        time.sleep(3)
        self.history.delete_pic()
        time.sleep(2)
        assert self.history.is_element_exist('Successfully deleted')
        self.history.ok()

    @allure.feature('test history page')
    @allure.story('test share photo')
    def test_share(self):
        self.history.open_pic(1)
        self.history.share()
        self.history.tw()
        with assume: assert self.history.is_element_exist('Share to')
        self.history.ins()
        with assume: assert self.history.is_element_exist('Share to')
        self.history.fb()
        with assume: assert self.history.is_element_exist('Share to')



