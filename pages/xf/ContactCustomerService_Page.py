#_*_coding:utf-8 -*-
#@Time     :2020/11/116:01
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :ContactCustomerService_Page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.xf.xf_page_locators import ContactCustomerService_Page_locator
class ContactCustomerServicePage(BasePage):

    def ContactCustomerService_Click_Recommender_Registration(self):
        """
        联系客服，点击推荐人登记
        :return:
        """
        self.Click_Eelement(ContactCustomerService_Page_locator.ContactCustomerService_Recommender_Registration,
                            "联系客服页面，点击推荐人登记")