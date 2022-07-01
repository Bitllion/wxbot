# -*- encoding: utf-8 -*-
"""
@文件        :schemas.py
@说明        :数据验证
@时间        :2022/06/30 11:34:43
@作者        :fanyq
@版本        :1.0
"""
from pydantic import BaseModel


class message(BaseModel):
    keyword: str
    message: str
    token: str


class token(BaseModel):
    token: str


class users(BaseModel):
    username: str
    password: str


# 修改密码多一个字段
class users_update(BaseModel):
    username: str
    old_password: str
    new_password: str
