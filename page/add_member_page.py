import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.contact_page import Contact


class AddMember(BasePage):
    _username ='username'
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")


    def add_member(self):
        """
        添加成员
        :return:
        """
        # self.driver.find_element(By.ID,self._username).send_keys("维恩")
        self.find(By.ID, 'username').send_keys("维恩")
        self.find(By.ID, 'memberAdd_acctid').send_keys("111222")
        self.find(By.ID, 'memberAdd_phone').send_keys("18911111111")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return Contact(self.driver)


    def add_member_fail(self):
        """
        添加成员失败
        :return:
        """
        # self.driver.find_element(By.ID, 'username').send_keys("维恩2")
        # self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("1112222")
        # self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("18911111111")
        # self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

        self.find(By.ID, self._username).send_keys("维恩2")
        self.find(By.ID, 'memberAdd_acctid').send_keys("1112222")
        self.find(By.ID, 'memberAdd_phone').send_keys("18911111111")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        #点击取消按钮
        self.find(By.CSS_SELECTOR,'.js_btn_cancel').click()
        return Contact(self.driver)