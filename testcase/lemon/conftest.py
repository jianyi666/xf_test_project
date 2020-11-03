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


@pytest.fixture(scope='class')
def lemon_login_class_fixture():
    dirver = Remote(Config.get("lemon_remote","command_executor"),
                    eval(Config.get("lemon_remote","desired_capabilities")))



@pytest.fixture
def lemon_login_case_fixture():
    pass






