import time

from page_object.page.BasePage import BasePage


class LoginPage(BasePage):

    _Apple_loc = 'value == "Continue with Apple"'
    _Google_loc =  'value CONTAINS "Google"'
    _Facebook_loc = 'label == "Continue with Facebook"'
    _Terms_loc = 'label == "Terms of Service"'
    _Privacy_loc = 'label == "Private Policy"'

    def loginByApple(self):
        self._continue_pwd = 'label == "使用密码继续"'
        self.find_element_predicate(self._Apple_loc).click()
        time.sleep(2)
        self.find_element_predicate(self._continue_pwd).click()

    def send_pwd(self,pwd):
        self.find_element_predicate('label == "%s"'% pwd).click()



    def loginByGoogle(self,account,pwd):
        self.find_element_predicate(self._Google_loc).click()

    def loginByFaceBook(self):
        self._continue_facebook = 'label == "继续"'
        self._open_facebook = 'label == "打开" AND name == "打开" AND type == "XCUIElementTypeButton"'
        self.find_element_predicate(self._Facebook_loc).click()
        self.find_element_predicate(self._continue_facebook).click()
        self.find_element_predicate(self._open_facebook).click()
        self.find_element_predicate(self._continue_facebook).click()
        self.ok()
        time.sleep(3)