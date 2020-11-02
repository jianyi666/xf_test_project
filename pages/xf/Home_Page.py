
from common.base_page import BasePage
from locator.xf.xf_page_locators import Home_Page_Locator
class HomePage(BasePage):

    def Home_Click_Notice_Close_Button(self):
        """
        点击首页公告的关闭按钮
        :return:
        """
        self.Wait_Element_Visibility(Home_Page_Locator.Home_Notice_Close_Button,"点击首页公告，关闭按钮")
        self.Click_Eelement(Home_Page_Locator.Home_Notice_Close_Button,"点击首页公告，关闭按钮")