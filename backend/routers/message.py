# -*- encoding: utf-8 -*-
"""
@文件        :message.py
@说明        :自定义关键词和消息
@时间        :2022/07/01 10:01:05
@作者        :fanyq
@版本        :1.0
"""
from fastapi import APIRouter
import models.crud as crud
from models.schemas import message, token
from libs.tokenFun import judgeToken, decodeToken

from config.settings import config
from loguru import logger

logger.remove()
logger.add(config.logger_db_path, format=config.logger_format, rotation="10 MB")

messageRouter = APIRouter()

# 修改message
@messageRouter.post("/message/update")
async def update_message(item: message):
    # 判断token
    if judgeToken(item.token):
        username = decodeToken(item.token)["username"]
        if crud.update_message(username, item.keyword, item.message):
            logger.info("{} update {} sucess", username, item.keyword)
            return {"code": 200, "msg": "update mesage sucess"}
        else:
            logger.info("{} update {} fail", username, item.keyword)
            return {"code": 400, "msg": "update mesage fail"}
    else:
        logger.info("token error")
        return {"code": 401, "msg": "token error"}


# 删除message
@messageRouter.post("/message/del")
async def delete_message(item: message):
    if judgeToken(item.token):
        username = decodeToken(item.token)["username"]
        if crud.delete_message(username, item.keyword):
            logger.info("{} del message-{} sucess", username, item.keyword)
            return {"code": 200, "msg": "delete success"}
        else:
            return {"code": 400, "msg": "delete failed"}
    else:
        return {"code": 401, "msg": "token is invalid"}


# 增加一条message
@messageRouter.post("/message/add")
async def add_message(item: message):
    # 判断token是否有效
    if judgeToken(item.token):
        # 解密username
        username = decodeToken(item.token)["username"]
        # token有效，添加message
        if crud.add_message(username, item.keyword, item.message):
            logger.info("ADD {}|{}|{}", username, item.keyword, item.message)
            return {"message": "success"}
        else:
            logger.error("ADD Failed: {} keyword is exist", username)
            return {"message": "keyword is exist"}
    else:
        logger.error("token is invalid")
        return {"message": "Token is invalid, please login again"}


# 查询message
@messageRouter.post("/message/query")
def query_message(item: message):
    # 判断token是否有效
    if judgeToken(item.token):
        # 解密username
        username = decodeToken(item.token)["username"]
        logger.info("QUERY {}", username)
        return crud.query_message(username)
    else:
        logger.error("token is invalid")
        return {"message": "Token is invalid, please login again"}
