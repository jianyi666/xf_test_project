from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from appium.webdriver import Remote
from common.handles_path import RESULT_XF_ERROR_SCREENSHOT_DIR,RESULT_XF_LOGS_DIR
from common.handles_logs import CreatLogs

import time
class BasePage():

    def __init__(self,driver:WebDriver,logfilepath):
        self.driver = driver
        self.log = CreatLogs(logfilepath)

    def Error_ScreenShot(self,filepath, filename):
        """
        错误后进行截图
        :param filepath:
        :return:
        """
        data_desc = time.strftime("%y-%m-%d_%H_%M_%S")
        path = filepath + "\\" + data_desc + "_" + filename + ".PNG"
        self.driver.save_screenshot(path)
    def Wait_Element_Clickable(self,ele,ele_desc,filepath):
        """
        等元素可以被点击
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable(ele))
        except Exception as e:
            self.Error_ScreenShot(filepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，可点击失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，可点击成功！")
    def Wait_Element_Presence(self,ele,ele_desc,filepath):
        """
        等待元素被加载
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(ele))
        except Exception as e:
            self.Error_ScreenShot(filepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，被加载失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，被加载成功！")

    def Wait_Element_Visibility(self,ele,ele_desc,filepath):
        """
        等元素可见
        :param ele:
        :param ele_desc:
        :return:
        """
        try:
            WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located(ele))
        except Exception as e:
            self.Error_ScreenShot(filepath,ele_desc)
            self.log.error(f"等待{ele_desc}元素，可见失败！")
            self.log.exception(e)
            raise e
        else:
            self.log.info(f"等待{ele_desc}元素，可见成功！")



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
        command_executor="http://127.0.0.1:9999/wd/hub",
        desired_capabilities = capabilities

    )
    driver.implicitly_wait(30)
    BP = BasePage(driver,RESULT_XF_LOGS_DIR)
    BP.Error_ScreenShot(RESULT_XF_ERROR_SCREENSHOT_DIR,"首页")



