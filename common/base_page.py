
from appium.webdriver.webdriver import WebDriver
from appium.webdriver import Remote
from common.handles_path import RESULT_XF_ERROR_SCREENSHOT_DIR
import time
class BasePage():

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def Error_ScreenShot(self,filepath, filename):
        """
        错误后进行截图
        :param filepath:
        :return:
        """
        data_desc = time.strftime("%y-%m-%d_%H_%M_%S")
        path = filepath + "\\" + data_desc + "_" + filename + ".PNG"
        self.driver.save_screenshot(path)




if __name__ == '__main__':
    capabilities = {
        "automationName": "UiAutomator2",
        # 设备操作系统
        "platformName": "Android",
        # 系统的版本
        "platformVersion": "6.0.1",
        # 设备名称(随意填写)
        "deviceName": "HuaWeiP30",
        # 应用程序的包名
        "appPackage": "com.foundersc.app.xf",
        # 应用程序的启动页面
        "appActivity": "com.hundsun.winner.application.hsactivity.splash.SplashActivity",
        "noReset": True
    }
    driver = Remote(
        command_executor="http://127.0.0.1:4327/wd/hub",
        desired_capabilities = capabilities

    )
    driver.implicitly_wait(30)
    BP = BasePage(driver)
    BP.Error_ScreenShot(RESULT_XF_ERROR_SCREENSHOT_DIR,"首页")



