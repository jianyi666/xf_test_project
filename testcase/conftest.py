#_*_coding:utf-8 -*-
#@Time     :2020/11/116:26
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :conftest.py
#@Sotfware :PyCharm

import pytest
from appium.webdriver import Remote
from common.handles_config import Config
from common.handles_path import RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR
from pages.xf.my_page import MyPage
from pages.xf.UserActivation_Page import UserActivationPage
from pages.xf.GeneralTransactionlogin_Page import GeneralTransactionloginPage



@pytest.fixture(scope="class")
def Login_Fixture():
    # 获取我的页面
    driver = Remote(Config.get("xf_remote","command_executor"),eval(Config.get("xf_remote","desired_capabilities")))
    my_page = MyPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    yield my_page
    driver.quit()






@pytest.fixture(scope="class")
def RecommenderRegistration_Fixture():
    driver = Remote(Config.get("xf_remote","command_executor"),eval(Config.get("xf_remote","desired_capabilities")))
    #获取我的页面
    my_page=MyPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 点击我的
    my_page.MyPage_Click_My()
    # 点击手机号登陆
    my_page.MyPage_Click_Moblie_Login()
    # 获取手机号激活页面
    useractivation_page = UserActivationPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 输入激活手机号
    useractivation_page.UserActivation_Input_Mobile(Config.get("xf_login_data","moblie_phone"))
    # 点击获取验证码
    useractivation_page.UserActivation_Click_Get_Verification_Code()
    # 输入验证码
    useractivation_page.UserActivation_Input_Verification_Code(Config.get("xf_login_data","verification_code"))
    # 点击验证手机
    useractivation_page.UserActivation_Click_Verify_Mobile()
    # 点击我的页面普通用户登录
    my_page.MyPage_Click_Mine_Login()
    # 获取普通用户登录页面
    generaltransactionlogin_page = GeneralTransactionloginPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 普通用户页面输入账号
    generaltransactionlogin_page.GeneralTransactionlogin_Input_Account(Config.get("xf_login_data","account"))
    # 普通用户页面输入密码
    generaltransactionlogin_page.GeneralTransactionlogin_Input_PassWord(Config.get("xf_login_data","password"))
    # 点击登录
    generaltransactionlogin_page.GeneralTransactionlogin_Click_Login()

    yield

    driver.quit()



