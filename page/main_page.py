import json
import os
import time

from selenium.webdriver.common.by import By
from page.add_member_page import AddMember
from page.base_page import BasePage
from page.contact_page import Contact
from utils.config import DATA_PATH


class MainPage(BasePage):
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self):
        #点击添加成员；进入通讯录页面
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()

        #添加通讯录页面打开的显示等待
        # 查找页面元素是否存在，如果存在返回 Ture, 如果不存在 返回False
        def wait(driver):
            ele_len = len(self.finds(By.ID, "username"))
            return ele_len >= 1
        # WebDriverWait(self.driver,10).until(wait)
        #自定义方法显示等待
        # self.wait_for(wait)

        #显示等待
        # self.wait_for_presence_of_element_located(By.CSS_SELECTOR, ".js_btn_continue")
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".js_btn_continue")
        return AddMember(self.driver)

    def goto_contact(self):
        return Contact(self.driver)

    def goto_improt_contact(self):
        pass


