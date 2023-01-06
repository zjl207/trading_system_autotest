# coding=utf-8
# @time: 2023/1/2 18:40
# Author: zjl
import yaml
from common.tools import get_project_path, sep


# file = open("C:/code/trading_system_autotest/config/environment.yaml",encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# with open("C:/code/trading_system_autotest/config/environment.yaml", "r", encoding="utf-8") as file:
#     # a = file.read()
#     for i in file.readlines():
#         print("=======")
#         print(i)
class GetConf:
    def __init__(self):
        """
        获取yaml文件内容
        """
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)  # 使用pyyaml获取yaml文件中内容
            # print(self.env)

    def get_username_password(self):
        """
        获取交易系统登录账号密码
        :return:
        """
        return self.env["username"], self.env["password"]

    def get_mysql(self):
        """
        获取mysql数据库配置
        :return:
        """
        return self.env["mysql"]
    def get_url(self):
        """
        获取跳转地址
        :return:
        """
        return self.env["url"]

# if __name__ == '__main__':
#     print(GetConf().get_url())
