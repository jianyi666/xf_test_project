#_*_coding:utf-8 -*-
#@Time     :2020/10/2922:31
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :handles_logs.py
#@Sotfware :PyCharm

import  logging
from logging.handlers import TimedRotatingFileHandler
from common.handles_path import RESULT_XF_LOGS_DIR
import time

def CreatLogs(filepath):
    # 创建一个日志收集器
    log = logging.getLogger("jianyi")

    #设置收集登录
    log.setLevel("INFO")

    data_desc = time.strftime("%y-%m-%d")
    file = filepath +"\\"+ data_desc +".log"
    # 设置按时间轮转的输出渠道
    fh = TimedRotatingFileHandler(filename= file,
                                  when='d',
                                  interval=7,
                                  backupCount=2,
                                  encoding="utf-8"
                                  )
    # 设置日志输出登录
    fh.setLevel("INFO")
    #将渠道添加到收集器
    log.addHandler(fh)

    # 设置日志输出格式
    format = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(format)
    fh.setFormatter(mate)
    return log

xf_log = CreatLogs(RESULT_XF_LOGS_DIR)

