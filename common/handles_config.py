#_*_coding:utf-8 -*-
#@Time     :2020/11/118:06
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :handles_config.py
#@Sotfware :PyCharm
from configparser import ConfigParser
from common.handles_path import CONF_DIR
import os
class HandlesConfig(ConfigParser):

    def __init__(self,filename,encoding='utf-8'):
        super().__init__()
        self.filename = filename
        self.encoding = encoding
        self.read(filename,encoding)


    def Write_Data(self,section,option,value):
        """
        配置文件中写入数据
        :param section:
        :param option:
        :param value:
        :return:
        """
        self.set(section,option,value)
        self.write(fp=open(self.filename,'w',encoding=self.encoding))

Config = HandlesConfig(os.path.join(CONF_DIR,"config.ini"))