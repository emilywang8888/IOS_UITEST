# import time
# import allure
# from page_object.page.LoginPage import LoginPage
#
#
# class TestLogin:
#
#     def setup_class(self):
#         self.login = LoginPage()
#
#     @allure.feature('test login')
#     @allure.story('test login with apple')
#     def test_login_apple(self):
#         self.login.loginByApple()
#         pwd = ('5','1','8','4','0','1')
#         for i in pwd:
#             self.login.send_pwd(i)
#         time.sleep(6)
#         assert self.login.is_element_exist("Home")
#
#     @allure.feature('test login')
#     @allure.story('test login with facebook')
#     def test_login_facebook(self):
#         self.login.loginByFaceBook()
#         assert self.login.is_element_exist("Home")
