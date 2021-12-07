import time
import allure
import pytest

from page_object.page.App import App
from page_object.page.LoginPage import LoginPage


class TestHomePage(object):
    
    @classmethod
    def setup_class(cls):
        cls.homePage = App.main()

    def setup_method(self):
        self.homepage = self.homePage.goto_myhomepage()
        time.sleep(2)

    def teardown_method(self):
        self.homepage.back()

    @allure.feature('test myhomepage')
    @allure.story('test click user manual')
    def test_user_manual(self):
        self.homepage.goto_User_manual()
        time.sleep(3)
        assert self.homepage.is_element_exist("FAQ")

    @allure.feature('test myhomepage')
    @allure.story('test click about us')
    def test_about_us(self):
        self.homepage.goto_about_us()
        time.sleep(2)
        assert self.homepage.is_element_exist("AI photo")

    @allure.feature('test myhomepage')
    @allure.story('test click terms of service')
    def test_terms(self):
        self.homepage.goto_Terms()
        assert self.homepage.is_element_exist("TERMS AND CONDITIONS")

    @allure.feature('test myhomepage')
    @allure.story('test click private policy')
    def test_policy(self):
        self.homepage.goto_Policy()
        assert self.homepage.is_element_exist("Welcome to Amemori")

    @allure.feature('test myhomepage')
    @allure.story('test change nickname')
    @pytest.mark.parametrize("nickname", ("Hi",))
    @pytest.mark.ios
    def test_nickname(self, nickname):
        self.homepage.change_nick_name(nickname)
        time.sleep(3)
        assert self.homepage.is_element_exist("Hi")

    @allure.feature('test myhomepage')
    @allure.story('test cancel nickname')
    @pytest.mark.parametrize("nickname", ("Hi",))
    def test_cancel_nickname(self, nickname):
        self.homepage.cancel_nick_name(nickname)
        time.sleep(2)

    @allure.feature('test myhomepage')
    @allure.story('test change avatar in six picture')
    @pytest.mark.parametrize("index", (0, 1, 2, 3, 4, 5))
    def test_avatar(self, index):
        self.homepage.goto_avatar(index)
        assert self.homepage.is_element_exist('Waiting')

    @allure.feature('test myhomepage')
    @allure.story('test change avatar from album')
    @pytest.mark.parametrize("index", (2,))
    def test_avatar_choose(self, index):
        self.homepage.change_avatar(index)
        time.sleep(10)
        assert self.homepage.is_element_exist('Edit Profile')


class TestContactUs(object):

    def setup_method(self):
        self.contact = App.main().goto_myhomepage().goto_contact_us()

    @allure.feature('test contact us')
    @allure.story('test contact us with facebook')
    def test_fb(self):
        self.contact.click_fb()
        time.sleep(2)
        assert self.contact.is_element_exist('Amemori AI Enhancer')

    @allure.feature('test contact us')
    @allure.story('test contact us with twitter')
    def test_tw(self):
        self.contact.click_tw()
        time.sleep(2)
        assert self.contact.is_element_exist('创建账号')

    @allure.feature('test myhomepage')
    @allure.story('test contact us with instagram')
    def test_ins(self):
        self.contact.click_ins()
        time.sleep(2)
        assert self.contact.is_element_exist('Amemoriapp')


class TestSignOut(object):

    @classmethod
    def setup_class(cls):
        cls.homePage = App.main()

    def setup_method(self):
        self.homepage = self.homePage.goto_myhomepage()
        time.sleep(2)

    @allure.feature('test logout')
    @allure.story('test cancel logout')
    def test_cancel_signout(self):
        self.homepage.cancel_signout()
        assert self.homePage.is_element_exist("Sign Out")

    # @allure.feature('test logout')
    # @allure.story('test logout success')
    # def test_signout(self):
    #     self.homepage.signout_success()
    #     assert LoginPage().is_element_exist("Google")
