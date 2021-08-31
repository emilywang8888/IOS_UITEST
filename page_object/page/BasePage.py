from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
# import cv2
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os, time
from page_object.driver.Client import IOSClient
from page_object.mylog.Log import MyLog
import yaml
import re

class BasePage(object):
    _back = 'label == "navback"'
    path = '/Users/wangqiaoling/Desktop/appiumfile/iOS_test_code/page_object/picture/'
    _skip = 'label contains "Skip"'
    _ok = 'label contains "OK"'



    def __init__(self):
        self.driver: WebDriver = self.getDriver()
        logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    @classmethod
    def getDriver(cls):
        cls.driver = IOSClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return IOSClient

    def find_element_xpath(self, xpath):
        for i in range(3):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                return element
            except:
                print('没有找到%s元素' % xpath)
        self.mylog('没有找到%s元素' % xpath)
        self.save_screen_shot()

    def find_element_predicate(self, value):
        for i in range(3):
            try:
                element = self.driver.find_element_by_ios_predicate(value)
                return element
            except:
                print('没有找到%s' % value)
        self.mylog(f'没有找到{value}元素')
        self.save_screen_shot()

    # 截图，出现错误截图保存
    def save_screen_shot(self, file_path = None):
        if file_path == None:
            project_path = os.path.dirname(os.getcwd())
            # print(project_path)
            file_path = project_path + "/images/"
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            images_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file_path = file_path + images_name + ".png"
            # print(file_path)
        self.driver.save_screenshot(file_path)

    # 写入日志
    def mylog(self, message):
        mylog = MyLog()
        mylog.error(message)

    # 判断元素是否存在
    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True

    # 回退键
    def back(self):
        self.find_element_predicate(self._back).click()

    def ok(self):
        self.find_element_predicate(self._ok).click()

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    # def skip(self):
    #     if self.is_element_exist(self._skip):
    #         self.driver.find_element_by_ios_predicate(self._skip).click()

    def drag(self, ele1, ele2):
        TouchAction(self.driver).press(ele1).wait(500).move_to(ele2).release().perform()

    # 坐标定位，暂时上传图片的从相册选择用这种方法
    def tap(self, x, y):
        self.driver.tap([(x, y)])

    # XPATH定位相册元素
    def find_element_ablum(self, loc):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, loc)))
            return element
        except:
            print(f'没有找到{loc}元素')
        self.mylog(f'没有找到{loc}元素')
        self.save_screen_shot()


    # 向上滑动
    def swipe_up(self, t=100, n=1):
        s = self.get_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)



    def find_image(self):
        self.driver.update_settings({"getMatchedImageResult": True})
        el = self.driver.find_element_by_image('path/to/img.ong')
        el.get_attribute('visual')  # returns base64 encoded string

    # def loadSteps(self, po_path, key, **kwargs):
    #     file=open(po_path, 'r')
    #     po_data=yaml.load(file)
    #     po_method=po_data[key]
    #     po_elements=dict()
    #     if po_data.keys().__contains__("elements"):
    #         po_elements=po_data['elements']
    #     #po_elements=yaml.load(open('xxx.yaml'))['elements']

        # for step in po_method:
        #     step: dict
        #     element_platform=dict()
        #     if step.keys().__contains__("element"):
        #         element_platform=po_elements[step['element']][IOSClient.platform]
        #     else:
        #         element_platform={"by": step['by'], "locator": step['locator']}
        #     element: WebElement=self.find(by=element_platform['by'], value=element_platform['locator'])
        #     action=str(step['action']).lower()
        #
        #     #todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
        #     if action=="click":
        #         element.click()
        #     elif action=="sendkeys":
        #         text=str(step['text'])
        #         for k,v in kwargs.items():
        #             origin=text
        #             text=text.replace("$%s" %k, v)
        #             print("update text: %s %s" % (origin, text))
        #         element.send_keys(text)
        #     else:
        #         print("UNKNOW COMMAND %s" % step)
        #
