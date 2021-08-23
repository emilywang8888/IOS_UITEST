import time
import pytest
import allure
from page_object.page.App import App


class TestFeedbackPage(object):

    @classmethod
    def setup_class(cls):
        cls.feedbackPage = App.main().goto_myhomepage()

    def setup_method(self):
        self.feedback = self.feedbackPage.goto_feedback()

    def teardown_method(self):
        self.feedback.ok()
        self.feedback.back()

    @allure.feature('test feedback')
    @allure.story('email is null')
    @pytest.mark.parametrize("email,content", [('','this is a test')])
    def test_feedback_email_empty(self,email,content):
        self.feedback.add_feedback(email,content)
        self.feedback.submit()
        time.sleep(2)
        assert self.feedback.is_element_exist('Email cannot be empty')

    @allure.feature('test feedback')
    @allure.story('content is null')
    @pytest.mark.parametrize("email,content", [('123@456.com', '')])
    def test_feedback_content_empty(self,email,content):
        self.feedback.add_feedback(email, content)
        self.feedback.submit()
        time.sleep(2)
        assert self.feedback.is_element_exist('Content cannot be empty')


    @allure.feature('test feedback')
    @allure.story('emali & content is not null, add 5 pictures')
    @pytest.mark.parametrize("email,content", [('123@163.com', 'this is a test content')])
    def test_submit_feedback(self,email,content):
        self.feedback.add_feedback(email,content)
        self.feedback.add_feedback_pic(5)
        self.feedback.submit()
        time.sleep(3)
        assert self.feedback.is_element_exist('Submitted Successfully')

