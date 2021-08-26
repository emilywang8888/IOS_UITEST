import time

from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class Contact_us(BasePage):

    _fb = 'label == "组 722"'  # 联系我们的fb   Amemori AI Enhancer
    _tw = 'label == "组 720"'  # 联系我们的tw   创建账号
    _ins = 'label == "组 721"'  # 联系我们的ins   Amemoriapp

    def click_fb(self):
        self.find_element_predicate(self._fb).click()

    def click_tw(self):
        self.find_element_predicate(self._tw).click()

    def click_ins(self):
        self.find_element_predicate(self._ins).click()




class MyHomePage(BasePage):

    _change_nick_name = 'label == "组 2162"'
    _user_manual = 'label == "User Manual"'
    _terms = 'label == "Terms of Service"'
    _policy = 'label == "Privacy Policy"'
    _about_us = 'label == "About Us"'
    _contact_us = 'label == "Contact Us"'
    _feedback = 'label == "Feedback"'
    _sign_out = 'label == "Sign Out"'
    _confirm_pic = 'label == "蒙版组 40"' # 更改头像时的√按钮地址
    _avater = '//*[contains(@name,"蒙版组")]/..' # 预设头像地址
    _nick_name_input = 'value == "Maximum 20 letters"'  # 修改昵称输入框
    _submit = '//*[contains(@name,"Submit")]/..'  # 提交按钮
    _cancel = 'label contains "Cancel"' # 取消修改昵称按钮
    _logout = 'label == "Log Out" AND name == "Log Out" AND type == "XCUIElementTypeButton"'  # 退出按钮
    _upload_pic = 'label contains "Upload a Photo"'  # 上传头像



    def goto_User_manual(self):
        self.find_element_predicate(self._user_manual).click()

    def goto_Terms(self):
        self.find_element_predicate(self._terms).click()

    def goto_Policy(self):
        self.find_element_predicate(self._policy).click()
        time.sleep(2)

    def goto_about_us(self):
        self.find_element_predicate(self._about_us).click()

    def goto_feedback(self):
        self.find_element_predicate(self._feedback).click()
        from page_object.page.FeedbackPage import Feedback
        return Feedback()

    def goto_avatar(self):
        self.find_element_xpath(self._avater).click()
        time.sleep(3)
        self.tap(50,320)

    def change_avatar(self):
        self.find_element_xpath(self._avater).click()
        self.find_element_predicate(self._upload_pic).click()
        x = self.get_size()['width']
        y = self.get_size()['height']
        time.sleep(2)
        self.tap(x / 3 / 2, (y - 300) / 4 + (y - 350) / 2)
        self.find_element_predicate(self._confirm_pic).click()

    def goto_contact_us(self):
        self.find_element_predicate(self._contact_us).click()
        return Contact_us()

    def signout_success(self):
        self.find_element_predicate(self._sign_out).click()
        self.find_element_predicate(self._logout).click()
        return LoginPage()

    def cancel_signout(self):
        self.find_element_predicate(self._sign_out).click()
        self.find_element_predicate(self._cancel).click()
        return MyHomePage()

    def change_nick_name(self,nickname):
        self.find_element_predicate(self._change_nick_name).click()
        if len(nickname) > 20:
            nickname = nickname[0,19]
        self.find_element_predicate(self._nick_name_input).send_keys(nickname)
        self.find_element_xpath(self._submit).click()
        # return MyHomePage()

    def cancel_nick_name(self,nickname):
        self.find_element_predicate(self._change_nick_name).click()
        self.find_element_predicate(self._nick_name_input).send_keys(nickname)
        self.find_element_predicate(self._cancel).click()
        # return MyHomePage()

    def go_back(self):
        self.back()
        return MyHomePage()
