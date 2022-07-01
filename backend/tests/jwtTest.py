# -*- encoding: utf-8 -*-
"""
@文件        :jwtTest.py
@说明        :测试jwt
@时间        :2022/07/01 10:39:15
@作者        :fanyq
@版本        :1.0
"""
import sys

sys.path.append("/home/bit/wxbot/backend/")
from libs.tokenFun import *

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2NDc5NzEsImlhdCI6MTY1NjY0NDM3MSwidXNlcm5hbWUiOiJyb290In0.U2kyCf4cJj37opuCzvtpNCOQXgbezZsPrt2Sh_JBEXU"

if judgeToken(token):  # 判断token是否有效
    print("token is valid")
    print(decodeToken(token))
else:
    print("token error")
