
from common.base_page import BasePage
from locator.xf.xf_page_locators import MyInformation_Page_Locator
import time
class MyInformationPage(BasePage):

    def MyInformation_Click_Mobile_Phone(self):
        """
        我的资料页面，点击手机号码
        :return:
        """
        self.Wait_Element_Visibility(MyInformation_Page_Locator.MyInformation_Mobile_Phone,"我的资料页面，点击手机号码")
        self.Click_Eelement(MyInformation_Page_Locator.MyInformation_Mobile_Phone,"我的资料页面，点击手机号码")