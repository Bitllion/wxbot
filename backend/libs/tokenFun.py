# -*- encoding: utf-8 -*-
"""
@文件        :jwt.py
@说明        :令牌的生成、解密、验证
@时间        :2022/06/30 14:29:38
@作者        :fanyq
@版本        :1.0
"""
import jwt
from datetime import datetime, timedelta
from config.settings import config
from models.crud import query_user


def genToken(username: str):
    """
    生成令牌
    :param username: 用户名
    :param secret_key: 密钥
    :param expire_time: 过期时间
    :return: 令牌
    """
    payload = {
        "exp": datetime.utcnow() + timedelta(seconds=config.token_expire_time),
        "iat": datetime.utcnow(),
        "username": username,
    }
    return jwt.encode(
        payload, config.token_secret_key, algorithm=config.token_algorithm
    )


def decodeToken(token: str):
    """
    解密令牌
    :param token: 令牌
    :param secret_key: 密钥
    :return: 解密后的令牌
    """
    return jwt.decode(
        token, config.token_secret_key, algorithms=[config.token_algorithm]
    )


def judgeToken(token: str):
    """
    判断令牌是否有效
    :param token: 令牌
    :return: True/False
    """
    try:
        decodeToken(token)
        if query_user(decodeToken(token)["username"]):
            return True
        else:
            return False
    except Exception as e:
        return False
