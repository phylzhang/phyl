# coding:utf-8
import os

# baidu测试地址
url_1 = "https://www.baidu.com/"

url_2 = "http://www.cnblogs.com/"


# 获取当前脚本的绝对路径， __file__是当前文件名
basepath = os.path.abspath(os.path.dirname(__file__))
# 用join去链接文件路径
report_path = os.path.join(basepath, "report")
case_path = os.path.join(basepath, "case")
data_path = os.path.join(basepath, "data")
image_path = os.path.join(basepath, "sreenshoot")

# 邮箱配置
sender_from = "xxx"
sender_pwd = "xxx"
# 收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com'
receive_to = "xxxx"
smtp_server = 'xxx'  # 收件服务器
