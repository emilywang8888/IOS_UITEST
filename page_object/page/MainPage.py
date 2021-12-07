from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage
from page_object.page.HistoryPage import HistoryPage
from page_object.page.MyHomePage import MyHomePage


class MainPage(BasePage):
    _History_loc = 'label == "History"'
    _My_homepage = 'label == "My Homepage"'
    _cartoon = 'label == "Cartoon Btn 01"'
    _private_img = 'name == "蒙版组 43"'
    _nick_name = 'value CONTAINS "user"'
    _one_click = 'label == "one click btn 02"'
    _coin_img = 'name == "jin_coin"'
    _coin = 'label == "5"'
    _halloween = 'label == "monster btn 03"'
    _avater = "//*[@type='XCUIElementTypeImage' and @name='蒙版组 43']/.."  # 预设头像地址

    def goto_history(self):
        self.find_element_predicate(MainPage._History_loc).click()
        return HistoryPage()

    def goto_myhomepage(self):
        self.find_element_predicate(MainPage._My_homepage).click()
        return MyHomePage()

    def cartoon(self):
        self.find_element_predicate(MainPage._cartoon).click()
        from page_object.page.UploadPage import UploadPage
        return UploadPage()

    def one_click(self):
        self.find_element_predicate(MainPage._one_click).click()
        from page_object.page.UploadPage import UploadPage
        return UploadPage()

    def halloween(self):
        self.find_element_predicate(MainPage._halloween).click()
        from page_object.page.UploadPage import UploadPage
        return UploadPage()




    # def gotoSelected(self):
    #     #调用全局的driver对象使用webdriver api操纵app
    #
    #     #self.driver.find_element(By.xpath, "//*[@text='自选']")
    #     zixuan="自选"
    #     self.findByText(zixuan)
    #     #self.driver.find_element_by_xpath("//*[@text='自选']")
    #     self.findByText(zixuan).click()
    #
    #     return SelectedPage()
    #
    # def gotoSearch(self) -> SearchPage:
    #     self.find(self._search_button).click()
    #     return SearchPage()
    #
    # def gotoProfile(self):
    #     #self.find(MainPage._profile_button).click()
    #     self.loadSteps("../data/MainPage.yaml", "gotoProfile")
    #     return ProfilePage()