from page_object.page.BasePage import BasePage
import time



class Feedback(BasePage):

    _submit_feedback = 'label contains "Submit"'  # 提交按钮
    _email = 'value == "Email"'  # 邮箱地址
    _feed_content = 'type == "XCUIElementTypeTextView"'  # 内容
    _add_pic = "//*[@type='XCUIElementTypeStaticText']/.."   # 添加图片的+号地址
    _add_pic_cancel = 'label == "取消"'      # 选择照片页的取消按钮
    _select_list = list('//*[@type="XCUIElementTypeImage"]')  # 照片列表
    _add_feed_pic = '//*[contains(@type,"TypeOther")]//*[contains(@type,"TypeImage")]/..'
    _feed_loc = 'label contains "We value your feedback"'  # 点击空白处让键盘消失
    _del_pic = '//*[@name="删除"]'  # 图片上的删除按钮
    _album_list = '//*[contains(@type,"TypeOther")]/*[contains(@type,"TypeImage")]'  # 相册列表



    def add_feedback(self,email,content):
        self.find_element_predicate(self._email).send_keys(email)
        self.find_element_predicate(self._feed_content).send_keys(content)
        self.find_element_predicate(self._feed_loc).click()

    def add_feedback_pic(self, index):
        for i in range(index):
            x = self.get_size()["width"]
            self.tap(x/5/2+i*(x/5),500)
            time.sleep(2)
            if i < 3:
                # print(self.get_size())
                self.tap(x/3/2+i*(x/3),210)
                time.sleep(2)
            else:
                self.tap(50+(i-2)*50,210+(i-2)*100)
                time.sleep(2)
            # album = self.find_element_ablum(self._album_list)
            # album[index].click()
        self.find_element_predicate(self._submit_feedback).click()
        time.sleep(3)


    def del_pic(self,index):
        if len(self._del_pic) > 0:
            self.find_element_predicate(self._del_pic[index]).click()
        return self

    def submit(self):
        self.find_element_predicate(self._submit_feedback).click()

