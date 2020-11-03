#_*_coding:utf-8 -*-
#@Time     :2020/11/116:26
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :conftest.py
#@Sotfware :PyCharm

import pytest
import time
from appium.webdriver import Remote
from common.handles_config import Config
from common.handles_path import RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR
from pages.xf.my_page import MyPage
from pages.xf.UserActivation_Page import UserActivationPage
from pages.xf.GeneralTransactionlogin_Page import GeneralTransactionloginPage
from pages.xf.ContactCustomerService_Page import ContactCustomerServicePage
from pages.xf.RecommenderRegistration_Page import RecommenderRegistrationPage
from pages.xf.MyInformation_Page import MyInformationPage
from pages.xf.LogOut_Page import LogOutPage
from pages.xf.Home_Page import HomePage

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
    # 获取首页
    home_page = HomePage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 首页关闭公告
    home_page.Home_Click_Notice_Close_Button()
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
    # 关闭我的页面广告弹窗
    my_page.MyPage_Click_Advertisement_Window_Close()
    # 滑动到联系客服可见
    my_page.MyPage_Swipe_To_Contact_Customer_Service_Visibility()
    # 点击联系客服
    my_page.MyPage_Click_Contact_Customer_Service()
    # 获取客户页面
    contactcustomerservice_page = ContactCustomerServicePage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 点击推荐人登记
    contactcustomerservice_page.ContactCustomerService_Click_Recommender_Registration()
    # 获取推荐人登记页面
    recommenderregistration_page = RecommenderRegistrationPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)

    yield recommenderregistration_page
    # 返回上一页面
    driver.press_keycode(4)
    time.sleep(1)
    driver.press_keycode(4)
    # 滑动到已登录手机号
    my_page.MyPage_Swipe_To_Signed_In_Mobile_Visibility()
    # 点击已登录手机号
    my_page.MyPage_Click_Signed_In_Mobile()
    # 获取我的资料页面
    myinformation_page = MyInformationPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 我的资料页面,点击手机号码
    myinformation_page.MyInformation_Click_Mobile_Phone()
    # 获取退出登录页面
    logout_page = LogOutPage(driver,RESULT_XF_LOGS_DIR,RESULT_XF_ERROR_SCREENSHOT_DIR)
    # 退出登录页面，点击退出登录
    logout_page.LogOut_Click_Log_Out()

    driver.quit()






