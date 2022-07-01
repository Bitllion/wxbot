# -*- encoding: utf-8 -*-
"""
@文件        :settings.py
@说明        :配置类
@时间        :2022/06/30 16:13:15
@作者        :fanyq
@版本        :1.0
"""
from configparser import ConfigParser
import os

BASE_DIR = os.path.dirname(__file__)
CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config.ini")


class Config(object):
    def __init__(self):
        config = ConfigParser()
        config.read(CONFIG_FILE_PATH)

        # token
        self.token_secret_key = config.get("token", "secret_key")
        self.token_expire_time = config.getint("token", "expire_time")
        self.token_algorithm = config.get("token", "algorithm")

        # logger
        self.logger_format = config.get("logger", "format")
        self.logger_db_path = config.get("logger", "db_path")


# 实例化
config = Config()

# test
if __name__ == "__main__":
    # 测试过期时间
    print(config.token_secret_key)
