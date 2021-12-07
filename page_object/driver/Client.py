from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml


class IOSClient(object):

    driver: WebDriver
    platform = "IOS"
    # platform = "iossimulator"

    @classmethod
    def install_app(cls) -> WebDriver:
        return cls.initDriver("install_app")

    @classmethod
    def restart_app(cls) -> WebDriver:
        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls, key):
        driver_data = yaml.load(open("../data/driver.yaml"))
        platform = str(driver_data['platform'])
        cls.platform = platform
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        caps = driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver
