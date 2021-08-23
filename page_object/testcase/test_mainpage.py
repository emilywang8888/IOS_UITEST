import time
from page_object.page.App import App
import allure


class TestMainPage:

    @classmethod
    def setup_class(cls):
        cls.mainpage=App.main()

    @allure.feature('go to history page')
    def test_history(self):
        self.mainpage.goto_history()
        time.sleep(5)
        assert self.mainpage.is_element_exist('History')

    @allure.feature('go to myhomepage')
    def test_homepage(self):
        self.mainpage.goto_myhomepage()
        time.sleep(2)
        assert self.mainpage.is_element_exist('User Manual')