from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from appium.webdriver import Remote
from common.handles_path import RESULT_XF_ERROR_SCREENSHOT_DIR,RESULT_XF_LOGS_DIR
from common.handles_logs import CreatLogs
from appium.webdriver.common.mobileby import MobileBy
import time
class BasePage():

    def __init__(self,driver:WebDriver,logfilepath,screenshotfilepath):
        self.driver = driver
        self.log = CreatLogs(logfilepath)
        self.screenshotfilepath =screenshotfilepath

    def Error_ScreenShot(self,filepath, filename):
        """
        错误后进行截图
        :param filepath:
        :return:
        """
        data_desc = time.strftime("%y-%m-%d_%H_%M_%S")
        path = filepath + "\\" + data_desc + "_" + filename + ".PNG"
        self.driver.save_screenshot(path)

    def Wait_Element_Clickable(self,ele,ele_desc):
        """
        等元素可以被点击
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable(ele))
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，可点击失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，可点击成功！")

    def Wait_Element_Presence(self,ele,ele_desc):
        """
        等待元素被加载
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(ele))
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，被加载失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，被加载成功！")

    def Wait_Element_Visibility(self,ele,ele_desc):
        """
        等元素可见
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located(ele))
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，可见失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，可见成功！")

    def Click_Eelement(self,ele,ele_desc):
        """
        点击元素，
        :param ele: 元素locator
        :param ele_desc: 元素描述
        :param filepath: 错误截图路径
        :return:
        """
        try:
            self.driver.find_element(*ele).click()
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath, ele_desc)
            self.log.error(f"{ele_desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"{ele_desc}，成功！")

    def Swipe_Element(self,ele,ele_desc,direction,count):
        """
        :param ele:元素定位器
        :param ele_desc:元素说明
        :param filepath: 错误截图保存位置
        :param direction:滑动方向 left right up down
        :return:
        """
        try:
            # 查找元素
            ele = self.driver.find_element(*ele)
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath, ele_desc)
            self.log.error(f"{ele_desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            # 获取组件的尺寸和坐标
            ele_size = ele.rect
            ele_height = ele_size["height"]
            ele_width = ele_size["width"]
            ele_x = ele_size["x"]
            ele_y = ele_size["y"]
            if direction.upper() in "UP":
                for i in count:
                    self.driver.swipe(start_x=ele_x+ele_width/2,start_y=ele_y+ele_height*0.9,end_x=ele_x+ele_width/2,end_y=ele_y+ele_height*0.1)
            elif direction.upper() in "DOWN":
                for i in count:
                    self.driver.swipe(start_x=ele_x+ele_width/2, start_y=ele_y+ele_height*0.1, end_x=ele_x+ele_width/2, end_y=ele_y+ele_height*0.9)
            elif direction.upper() in "LEFT":
                for i in count:
                    self.driver.swipe(start_x=ele_x+ele_width*0.9, start_y=ele_y+ele_height/2, end_x=ele_x+ele_width*0.1, end_y=ele_y+ele_height/2)
            elif direction.upper() in "RIGHT":
                for i in count:
                    self.driver.swipe(start_x=ele_x+ele_width*0.1, start_y=ele_y+ele_height/2, end_x=ele_x+ele_width*0.9, end_y=ele_y+ele_height/2)
            self.log.info(f"{ele_desc}，成功！")

    def Swipe_Element_To_Visibility(self,target_ele,target_ele_desc,top_ele,bottom_ele):
        """
        滑动到目标元素可见
        :param target_ele: 目标元素
        :param target_ele_desc: 目标元素说明
        :param top_ele: 顶部元素
        :param bottom_ele: 底部元素
        :return:
        """
        window_size = self.driver.get_window_size()
        height = window_size["height"]
        width = window_size["width"]
        down =True
        count = 0
        while down:
            try:
                self.driver.find_element(*target_ele)
                self.log.info(f"向下第{count}次,{target_ele_desc},成功！")
                down = False
                break
            except Exception as e:
                try:
                    self.driver.find_element(*top_ele)
                    down = False
                    break
                except Exception as e:
                    self.driver.swipe(start_x=width / 2, start_y=height / 2, end_x=width / 2, end_y=height / 2 + 500)
                    count += 1
                    self.log.error(f"向下第{count}次,{target_ele_desc},失败！")
        up = True
        count = 0
        while up:
            try:
                self.driver.find_element(*target_ele)
                self.log.info(f"向上第{count}次,{target_ele_desc},成功！")
                up = False
                break
            except Exception as e:
                try:
                    self.driver.find_element(*bottom_ele)
                    up = False
                    break
                except Exception as e:
                    self.driver.swipe(start_x=width / 2, start_y=height / 2, end_x=width / 2, end_y=height / 2 - 500)
                    count += 1
                    self.log.error(f"向上第{count}次,{target_ele_desc},失败！")

    def Input_Element_SendKeys(self,target_ele,target_ele_desc,value):
        """
        向元素中输入文本
        :param target_ele: 目标元素
        :param target_ele_desc: 目标元素描述
        :param value: 输入的内容
        :return:
        """
        try:
            self.driver.find_element(*target_ele).send_keys(value)
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath, target_ele_desc)
            self.log.error(f"{target_ele_desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"{target_ele_desc}，成功！")

    def Get_Element_Attribute(self,target_ele,target_ele_desc,attribute):
        """
        获取元素的，属性
        :return:
        """
        try:
            attr = self.driver.find_element(*target_ele).get_attribute(attribute)
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath, target_ele_desc)
            self.log.error(f"{target_ele_desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"{target_ele_desc}，成功！")
            return attr

    def Get_Element_Attribute_From_Text(self,value,attribute,desc):
        """
        通过输入信息查找元素，获取元素的属性
        :param value:
        :param attr:
        :return:
        """
        locator = (MobileBy.XPATH, f'//*[cotains(@text,"{value}")]')
        try:
            attr = self.driver.find_element(*locator).get_attribute(attribute)
        except Exception as e:
            self.Error_ScreenShot(self.screenshotfilepath, desc)
            self.log.error(f"{desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"{desc}，成功！")
            return attr

    def Switch_To_WebView(self,WebView_Name,desc):
        """
        切换到目标WebView
        :param WebView_Name:
        :param loc_desc:
        :return:
        """

        try:
            self.driver.switch_to.context(WebView_Name)
        except Exception as e :
            self.Error_ScreenShot(self.screenshotfilepath, desc)
            self.log.error(f"{desc}，失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"{desc}，成功！")

    def Switch_To_windows(self,target_ele,target_ele_desc):
        """
        切换到目标windows
        :param target_ele:
        :param target_ele_desc:
        :return:
        """
        # 获取所有的句柄
        wins = self.driver.window_handles
        # 遍历所有窗口的句柄，依次进行切换，查找该窗口是否有
        for win in wins:
            self.driver.switch_to.window(win)
            try:
                WebDriverWait(driver,3,0.5).until(EC.visibility_of_element_located(target_ele))
            except Exception as e:
                pass
            else:
                self.log.info(f"{target_ele_desc},成功！")
                break
        else:
            self.log.info(f"{target_ele_desc},失败！")
            self.Error_ScreenShot(self.screenshotfilepath, target_ele_desc)





if __name__ == '__main__':
    capabilities = {
        "automationName": "UiAutomator2",
        # 设备操作系统
        "platformName": "Android",
        # 系统的版本
        "platformVersion": "7.1.2",
        # 设备名称(随意填写)
        "deviceName": "HuaWeiP30",
        # 应用程序的包名
        "appPackage": "com.foundersc.app.xf",
        # 应用程序的启动页面
        "appActivity": "com.hundsun.winner.application.hsactivity.splash.SplashActivity",
        "noReset": True
    }
    driver = Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        desired_capabilities = capabilities

    )

    BP = BasePage(driver,RESULT_XF_LOGS_DIR)
    ele =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/tv_news_title")')
    top =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/search_layout")')
    bottom =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/bigData_layout")')
    time.sleep(6)
    BP.Swipe_Element_To_Visibility(ele,"滑动首页面，广告位可见",top,bottom)



