#_*_coding:utf-8 -*-
#@Time     :2020/10/3022:28
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :xf_page_locators.py
#@Sotfware :PyCharm
from appium.webdriver.common.mobileby import MobileBy

# 我的页面
class my_page_Locator():
    # 底部我的
    MyPage_Bottom_my = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/tv_mine")')
    # 手机登录
    MyPage_Moblie_Login = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_activate_phone_tv")')
    # 普通交易登录
    MyPage_Mine_Login = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_login_ll")')
    # 联系客服
    MyPage_Contact_Customer_Service =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("联系客服")')
    # 我的页面顶部
    MyPage_Top_Locator =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/mine_member_togo_rl")')
    # 我的页面顶部
    MyPage_Bottom_Locator = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("联系客服")')

# 联系客服页面
class ContactCustomerService_Page_locator():
    # 登记推荐人
    ContactCustomerService_Recommender_Registration =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("推荐人登记")')


# 用户激活页面
class UserActivation_Page_Locator():
    # 输入手机号
    UserActivation_Moblie = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入11位中国大陆手机号")')
    # 获取验证码
    UserActivation_Get_Verification_Code =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("获取验证码")')
    # 输入验证码
    UserActivation_Verification_Code = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入验证码")')
    # 验证手机
    UserActivation_Verify_Mobile = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("验证手机")')

# 普通用户登录页面
class GeneralTransactionlogin_Page_Locator():
    # 输入用户账号
    GeneralTransactionlogin_Account = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入普通交易账号")')
    # 输入登录密码
    GeneralTransactionlogin_PassWord =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("交易密码")')
    # 点击登录按钮
    GeneralTransactionlogin_Login_button =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.LinearLayout")')

# 推荐人登记页面
class RecommenderRegistration_Page_Locator():
    # 推荐人登记页面，产品信息
    RecommenderRegistration_Product_Information =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/et_financial_pro_message")')
    # 推荐人登记页面，推荐人
    RecommenderRegistration_Recommender = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/et_financial_recomen")')
    # 推荐人登记页面，提交
    RecommenderRegistration_Submit = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/bt_final_comment_submit_un")')
    # 推荐人，姓名
    RecommenderRegistration_Recommender_Name =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/tv_financial_result_name")')
    # 推荐人，营业部地址
    RecommenderRegistration_Recommender_Address =(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.foundersc.app.xf:id/tv_financial_result_address")')

