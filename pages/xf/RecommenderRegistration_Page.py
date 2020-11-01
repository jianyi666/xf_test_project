#_*_coding:utf-8 -*-
#@Time     :2020/11/116:32
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :RecommenderRegistration_Page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.xf.xf_page_locators import RecommenderRegistration_Page_Locator

class RecommenderRegistrationPage(BasePage):

    def RecommenderRegistration_Input_Product_Code(self,value):
        """
        推荐人登记页面，输入产品代码
        :param value:
        :return:
        """
        self.Input_Element_SendKeys(RecommenderRegistration_Page_Locator.RecommenderRegistration_Product_Information,
                                    "推荐人登记页面，输入产品代码",value)

    def RecommenderRegistration_Input_Recommender(self,value):
        """
        推荐人登记页面，输入推荐人
        :param value:
        :return:
        """
        self.Input_Element_SendKeys(RecommenderRegistration_Page_Locator.RecommenderRegistration_Recommender,
                                    "推荐人登记页面，输入推荐人手机号",value)

    def RecommenderRegistration_Click_Submit(self):
        """
        推荐人登记页面，点击提交
        :return:
        """
        self.Click_Eelement(RecommenderRegistration_Page_Locator.RecommenderRegistration_Submit,"推荐人登记页面，点击提交")

    def RecommenderRegistration_Get_Recommender_Name(self):
        """
        推荐人登记页面，获取推荐人姓名
        :return:
        """
        return self.Get_Element_Attribute(RecommenderRegistration_Page_Locator.RecommenderRegistration_Recommender_Name,
                                           "推荐人登记页面，获取推荐人姓名","text")

    def RecommenderRegistration_Get_Recommender_Address(self):
        """
        推荐人登记页面，获取推荐人地址
        :return:
        """
        return self.Get_Element_Attribute(RecommenderRegistration_Page_Locator.RecommenderRegistration_Recommender_Address,
                                           "推荐人登记页面，获取推荐人地址","text")

    def RecommenderRegistration_Get_History_Recommender_Information(self,Name,desc):
        """
        推荐人登记页面，获取历史推荐人信息
        :return:
        """
        return self.Get_Element_Attribute_From_Text(Name,"text",desc)

