#_*_coding:utf-8 -*-
#@Time     :2020/10/3022:21
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :my_page.py
#@Sotfware :PyCharm
from common.handles_path import RESULT_XF_ERROR_SCREENSHOT_DIR
from common.base_page import BasePage
from locator.xf.xf_page_locators import my_page_Locator
class MyPage(BasePage):

    def MyPage_Click_My(self):
        """
        点击底部，我的，进入我的页面
        :return:
        """
        self.Wait_Element_Visibility(my_page_Locator.MyPage_Bottom_my,"点击底部，我的进入页面")
        self.Click_Eelement(my_page_Locator.MyPage_Bottom_my,"点击底部我的，进入页面")

    def MyPage_Click_Moblie_Login(self):
        """
        我的页面，点击手机登录
        :return:
        """
        self.Click_Eelement(my_page_Locator.MyPage_Moblie_Login,"我的页面，点击手机登录页面")

    def MyPage_Click_Mine_Login(self):
        """
        我的页面，点击登录账号
        :return:
        """
        self.Click_Eelement(my_page_Locator.MyPage_Mine_Login,"我的页面，点击账户登录")

    def MyPage_Swipe_To_Contact_Customer_Service_Visibility(self):
        """
        我的页面，滑动到联系客服可见
        :return:
        """
        self.Swipe_Element_To_Visibility(my_page_Locator.MyPage_Contact_Customer_Service,"我的页面，滑动到联系客服可见",
                                         my_page_Locator.MyPage_Top_Locator,my_page_Locator.MyPage_Bottom_Locator
                                         )





