from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
# 生成一个浏览器（webdriver对象）:反射机制
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

# 定义工具类
class Webkey:
    # 构造函数
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    # 访问URL:wk.open(**args)
    def open(self, **kwargs):
        self.driver.get(kwargs['send_text'])
        self.driver.maximize_window()

    #退出
    def quit(self,**kwargs):
        self.driver.quit()
    #元素定位
    def locator(self,**kwargs):
        try:
           return self.driver.find_element(kwargs['name'],kwargs['values'])
        except:
            print('用例执行失败')
    #层级定位
    def locator_s(self,**kwargs):
        print(kwargs['send_text'])
        return self.driver.find_elements(kwargs['name'],kwargs['values'])[int(kwargs['send_text'])]

    #输入
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['send_text'])
    #点击
    def clicks(self,**kwargs):
        self.locator_s(**kwargs).click()
    #点击
    def click(self,**kwargs):
        self.locator(**kwargs).click()

    #文本校验
    def assert_text(self,**kwargs):
        try:
            assert self.locator(**kwargs).text == kwargs['yq_text']
            return True
        except:
            return False

    #获取元素属性进行断言
    def assert_att(self,**kwargs):
        try:
            # get_attribute('元素名')  获取元素值
            assert self.locator(**kwargs).get_attribute(kwargs['send_text']) == str(kwargs['yq_text'])
            return True
        except:
            return False
    # 切换浏览器句柄（不关闭原标签）
    def switch_handles(self,**kwargs):
        handles = self.driver.window_handles  # 获取浏览器句柄（标签页）
        self.driver.switch_to.window(handles[1])

    # 切换浏览器句柄，并关闭原标签
    def switch_close_handles(self,**kwargs):
        handles = self.driver.window_handles  # 获取浏览器句柄（标签页）
        self.driver.close()                   # 关闭原标签
        self.driver.switch_to.window(handles[1])

    # 切换到原浏览器句柄
    def switch_old_handles(self, **kwargs):
        handles = self.driver.window_handles  # 获取浏览器句柄（标签页）
        self.driver.switch_to.window(handles[0])

    #获取title
    def get_title(self,**kwargs):
        print(self.driver.title)

    #切换到iframe
    def cut_iframe(self,**kwargs):
        # iframe = self.driver.find_element(kwargs['name'],kwargs['values'])  # 获取iframe元素
        self.driver.switch_to.frame(self.locator(**kwargs))  # 切换到iframe页面中

    #退出iframe
    def quit_iframe(self, **kwargs):
        self.driver.switch_to.default_content()

     #强制等待
    def wait_time(self,**kwargs):
        sleep(int(kwargs['send_text']))

    #显示等待
    def visit_wait(self,**kwargs):
        try:
            WebDriverWait(self.driver,kwargs['send_text'],0.5).until(
                lambda el: self.locator(**kwargs),message='查找元素失败')
            return True
        except:
            return False
     #悬停
    def hover(self,**kwargs):
        el=self.locator(**kwargs)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()
    '''
    click:鼠标左击
    double_click：鼠标双击
    context_click：鼠标右击
    drag_and_drop_by_offset(元素)   在元素处 按住鼠标左键
    '''
    #局部左右滑动
    def Sliding_around(self,**kwargs):
        wd = self.locator(**kwargs)
        sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(wd, int(kwargs['send_text']), 0).perform()

    # 局部左右滑动
    def up_down(self, **kwargs):
        wd = self.locator(**kwargs)
        sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(wd, 0, int(kwargs['send_text'])).perform()
    #鼠标滚轮滑动
    def swipe(self,**kwargs):
        js="var q=document.documentElement.scrollTop={}".format(1000)
        self.driver.execute_script(js)


