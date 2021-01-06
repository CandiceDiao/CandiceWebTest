from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Contact(BasePage):

    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")



    def get_member(self):
        #find_elements:返回为一个list
        elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')

        # 如下结构可以写为列表推导式
        # member_list = []
        # for element in elements:
        #     member_list.append(element.get_attribute("title"))
        return [element.get_attribute("title") for element in elements]