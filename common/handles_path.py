import os


Base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# COMMON DIR
COMMON_DIR = os.path.join(Base_url,"common")
# CONF DIR
CONF_DIR = os.path.join(Base_url,"conf")
# DATA_DIR
DATA_XF_DIR = os.path.join(Base_url,r"data\xf")
# LOCATOR_DIR
LOCATOR_XF_DIR = os.path.join(Base_url,r"locator\xf")
# PAGES_DIR
PAGE_XF_DIR = os.path.join(Base_url,r"pages\xf")
# RESULT_DIR
RESULT_XF_ERROR_SCREENSHOT_DIR = os.path.join(Base_url,r"result\xf\error_screenshot")
RESULT_XF_LOGS_DIR = os.path.join(Base_url,r"result\xf\logs")
RESULT_XF_REPORTS_DIR = os.path.join(Base_url,r"result\xf\reports")
# TESTCASE_DIR
TESTCASE_XF_DIR = os.path.join(Base_url,r"result\testcase\xf")

