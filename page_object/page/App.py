
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        # cls.getClient().install_app()
        cls.getClient().restart_app()
        return MainPage()