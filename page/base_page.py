import json
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# BasePage定义，它是一个其他page的公共方法的封装，它是一个底层使用的框架
from utils.config import DATA_PATH


class BasePage():
    _base_url = ""
    # 拼接文件路径待封装
    _filepath =os.path.join(DATA_PATH,'cookies.json')

    # 参数中的driver要指定类型，python才能识别
    def __init__(self, driver:WebDriver=None,reuse=False):
        #让python编译器知道有一个实例变量：driver
        self.driver=None
        if driver is None and reuse == True:
            # 如果发现driver是空，reuse标志位为True->就复用已有的浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
        elif driver is None and reuse == False:
            # 如果发现driver是空，reuse标志位为False->new chrome driver
            self.driver = webdriver.Chrome()
        else:
            # 如果发现driver不为空时，无需再次创建
            self.driver=driver

        if self._base_url != "":
            self.driver.get(self._base_url)
        # 隐式等待，解决元素加载过慢的问题
        self.driver.implicitly_wait(3)


    # 获取cookies
    def get_cookies(self):
        time.sleep(15)
        #手动进行扫码，获取cookie
        # 获取到的cookies为一个列表list
        cookies = self.driver.get_cookies()
        #将获取到的cookies写入文件
        #使用json文件，因为进行格式转换
        with open(self._filepath,"w")as f:
            json.dump(cookies,f)

    #添加cookie
    def add_cookie(self):
        #从文件中读取保存的cookies
        with open(self._filepath,"r")as f:
            cookies = json.load(f)
        #由于取到的cookies为一个list【dict】，而add_cookie()需要传入dict
        #需要循环遍历cookies取出里面的dict
        for cookie in cookies:
            # 添加一个dict的cookie信息
            # 由于selenium的cookies不支持expiry，所以需要去掉
            if "expiry" in cookie.keys():
                # dict支持pop的删除函数
                cookie.pop("expiry")
            # 把cookie键值对一个一个塞入浏览器中
            else:
                self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = self.wait_for_element_to_be_clickable(By.ID, "menu_index")
            # 如果找到元素说明已经进入页面，跳出循环
            # 否则要继续刷新页面
            if res is not None:
                break

    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)

    def finds(self,by,value):
        return self.driver.find_elements(by=by,value=value)

    # 封装自定义方法的显示等待
    def wait_for(self,fun):
        # 参数fun 为布尔类型
        #fun 为True 结束显示等待 继续执行
        #fun 为Flase 继续轮询查找元素
        WebDriverWait(self.driver, 10).until(fun)

    # 封装显示等待：元素可见
    def wait_for_presence_of_element_located(self,*args):
        return WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(*args))


    # # 封装显示等待：元素可点击
    #*args 将传入的参数打包成元组
    def wait_for_element_to_be_clickable(self,*args):
        return WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(args))

    def quit(self):
        self.driver.quit()



