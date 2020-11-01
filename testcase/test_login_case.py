#_*_coding:utf-8 -*-
#@Time     :2020/11/118:49
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_login_case.py
#@Sotfware :PyCharm

import pytest
from data.xf.login_test_data import Login_Error_Data
class Test_Login():

    @pytest.mark.parametrize("cases",Login_Error_Data)
    def test_login_error_infor(self,cases,Login_Fixture):

        mypage = Login_Fixture
        # 点击 手机登录
        mypage.MyPage_Click_Moblie_Login()
