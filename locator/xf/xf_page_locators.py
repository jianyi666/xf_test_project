#_*_coding:utf-8 -*-
#@Time     :2020/10/3022:28
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :xf_page_locators.py
#@Sotfware :PyCharm
from appium.webdriver.common.mobileby import MobileBy

class my_page_Locator():

    MyPage_Bottom_my = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/tv_mine")')
    MyPage_Moblie_Login = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_activate_phone_tv")')
    MyPage_Mine_Login = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_login_ll")')
    MyPage_Contact_Customer_Service =(MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().text("联系客服")')
    MyPage_Top_Locator =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_member_togo_rl")')
    MyPage_Bottom_Locator = (MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().text("联系客服")')

class UserActivation_Page_Locator():
    UserActivation_Moblie = (MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().text("请输入11位中国大陆手机号")')
    UserActivation_Get_Verification_Code =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("获取验证码")')
    UserActivation_Verification_Code = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入验证码")')
    UserActivation_Verify_Mobile = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("验证手机")')

class GeneralTransactionlogin_Page_Locator():
    GeneralTransactionlogin_Account = (MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().text("请输入普通交易账号")')
    GeneralTransactionlogin_PassWord =(MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().text("交易密码")')
    GeneralTransactionlogin_Login_button =(MobileBy.ANDROID_UIAUTOMATOR,'new Uiselector().class("android.widget.LinearLayout")')
