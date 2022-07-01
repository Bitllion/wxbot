# -*- encoding: utf-8 -*-
"""
@文件        :hello.py
@说明        :测试helloworld 
@时间        :2022/06/30 11:47:27
@作者        :fanyq
@版本        :1.0
"""
from fastapi import APIRouter
from libs.tokenFun import judgeToken, decodeToken
from models.schemas import token

helloworld = APIRouter()


@helloworld.get("/helloworld")
async def hello(item: token):
    if judgeToken(item.token):
        return {
            "message": "hello world! Welcome {}".format(
                decodeToken(item.token)["username"]
            )
        }
