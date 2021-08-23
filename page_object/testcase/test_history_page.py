import time
import allure
import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage

class TestHistory(object):
    @classmethod
    def setup_class(cls):
        cls.historyPage = App.main()

    def setup_method(self):
        self.history=self.historyPage.goto_history()
        time.sleep(10)

    @allure.feature('test history page')
    @allure.story('test swipe up')
    @pytest.mark.parametrize("n",(5,))
    def test_swipe(self,n):
        self.history.swipe_screen(n)

    @allure.feature('test history page')
    @allure.story('test delete photo')
    @pytest.mark.skip
    def test_del(self):
        self.history.open_pic()
        self.history.delete_pic()
        assert self.history.is_element_exist('deleted')

    @allure.feature('test history page')
    @allure.story('test share photo')
    @pytest.mark.skip
    def test_share(self):
        self.history.open_pic()
        self.history.share()
        assert self.history.is_element_exist('Facebook')

    @allure.feature('test history page')
    @allure.story('test download photo')
    @pytest.mark.skip
    def test_download(self):
        self.history.open_pic()
        self.history.download_pic()
        assert self.history.is_element_exist('successfully')
