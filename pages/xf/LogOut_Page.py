from common.base_page import BasePage
from locator.xf.xf_page_locators import LogOut_Page_Locator
import time
class LogOutPage(BasePage):

    def LogOut_Click_Log_Out(self):
        """
        退出登录页面点击退出登录
        :return:
        """
        self.Wait_Element_Visibility(LogOut_Page_Locator.LogOut_logout,"退出登录页面，点击退出登录")
        self.Click_Eelement(LogOut_Page_Locator.LogOut_logout,"退出登录页面，点击退出登录")
