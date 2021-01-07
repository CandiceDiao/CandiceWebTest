from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# BasePage定义，它是一个其他page的公共方法的封装，它是一个底层使用的框架
class BasePage():
    _base_url = ""

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
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(*args))


    # # 封装显示等待：元素可点击
    #*args 将传入的参数打包成元组
    def wait_for_element_to_be_clickable(self,*args):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(args))

    def quit(self):
        self.driver.quit()



