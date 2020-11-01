#_*_coding:utf-8 -*-
#@Time     :2020/11/116:05
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :UserActivation_Page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.xf.xf_page_locators import UserActivation_Page_Locator
class UserActivationPage(BasePage):

    def UserActivation_Input_Mobile(self,value):
        """
        用户激活页面，输入手机号
        :param value:
        :return:
        """
        self.Wait_Element_Visibility(UserActivation_Page_Locator.UserActivation_Moblie,"用户激活页面，输入手机号")
        self.Input_Element_SendKeys(UserActivation_Page_Locator.UserActivation_Moblie,"用户激活页面，输入手机号",value)


    def UserActivation_Input_Verification_Code(self,value):
        """
        用户激活页面，输入验证码
        :param value:
        :return:
        """
        self.Wait_Element_Visibility(UserActivation_Page_Locator.UserActivation_Verification_Code,"用户激活页面，输入验证码")
        self.Input_Element_SendKeys(UserActivation_Page_Locator.UserActivation_Verification_Code,"用户激活页面，输入验证码",value)

    def UserActivation_Click_Get_Verification_Code(self):
        """
        用户激活页面，点击获取验证码
        :return:
        """
        self.Wait_Element_Clickable(UserActivation_Page_Locator.UserActivation_Get_Verification_Code,"用户激活页面，点击获取验证码")
        self.Click_Eelement(UserActivation_Page_Locator.UserActivation_Get_Verification_Code,"用户激活页面，点击获取验证码")

    def UserActivation_Click_Verify_Mobile(self):
        """
        用户激活页面，点击验证手机
        :return:
        """
        self.Wait_Element_Clickable(UserActivation_Page_Locator.UserActivation_Verify_Mobile,"用户激活页面，点击验证手机")
        self.Click_Eelement(UserActivation_Page_Locator.UserActivation_Verify_Mobile,"用户激活页面，点击验证手机")