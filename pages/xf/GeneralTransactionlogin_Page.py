#_*_coding:utf-8 -*-
#@Time     :2020/11/116:15
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :GeneralTransactionlogin_Page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.xf.xf_page_locators import GeneralTransactionlogin_Page_Locator

class GeneralTransactionloginPage(BasePage):


    def GeneralTransactionlogin_Input_Account(self,value):
        """
        普通交易账号登录页面，输入账号
        :return:
        """
        self.Wait_Element_Visibility(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_Account,"普通交易登录页面，输入用户账号")
        self.Input_Element_SendKeys(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_Account,"普通交易登录页面，输入用户账号",value)


    def GeneralTransactionlogin_Input_PassWord(self,value):
        """
        普通交易账号登录页面，输入密码
        :param value:
        :return:
        """
        self.Wait_Element_Visibility(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_PassWord,"普通交易登录页面，输入用户密码")
        self.Input_Element_SendKeys(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_PassWord,"普通交易登录页面，输入用户密码",value)

    def GeneralTransactionlogin_Click_Login(self):
        """
        普通交易账号登录页面，点击登录
        :return:
        """
        self.Wait_Element_Clickable(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_Login_button,"普通交易登录页面，点击登录按钮")
        self.Click_Eelement(GeneralTransactionlogin_Page_Locator.GeneralTransactionlogin_Login_button,"普通交易登录页面，点击登录按钮")