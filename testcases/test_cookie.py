"""
获取登录二维码 cookie
"""
from page.main_page import MainPage


class TestCookie:

    def setup(self):
        self.main = MainPage()

    def test_get_cookie(self):
        self.main.get_cookies()

    def teardown(self):
        self.main.quit()

