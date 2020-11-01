#_*_coding:utf-8 -*-
#@Time     :2020/11/116:29
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_recommender_registration_page_case.py
#@Sotfware :PyCharm
import pytest
from data.xf.recommenderregistration_test_data import RecommenderRegistration_Error_Data
class Test_RecommenderRegistration():

    @pytest.mark.parametrize("cases",RecommenderRegistration_Error_Data)
    def test_input_errot_product_code(self,cases,RecommenderRegistration_Fixture):
        pass


if __name__ == '__main__':
    pytest.main(["-s", "test_recommender_registration_page_case.py"])