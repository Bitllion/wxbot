# -*- encoding: utf-8 -*-
"""
@文件        :users.py
@作者        :fanyq
@版本        :1.0
"""
from fastapi import APIRouter
from models.schemas import users, users_update
import models.crud as crud
from libs.tokenFun import genToken
from config.settings import config
from loguru import logger

logger.remove()
logger.add(config.logger_db_path, format=config.logger_format, rotation="10 MB")

usersRouter = APIRouter()

# 用户登录
@usersRouter.post("/users/login")
async def login(item: users):
    if crud.query_user(item.username):
        if crud.query_user(item.username)["password"] == item.password:
            # 生成jwt令牌
            token = genToken(item.username)
            logger.info("{} login success".format(item.username))
            return {"message": "登录成功", "token": token}
        else:
            logger.error(
                "{} login failed, beacause password is wrong".format(item.username)
            )
            return {"message": "密码错误，登录失败"}
    else:
        logger.error("{} login failed, because user is not exsit".format(item.username))
        return {"message": "用户不存在，登录失败"}


# 用户注册
@usersRouter.post("/users/register")
async def register(item: users):
    if crud.add_user(item.username, item.password):
        logger.info("{} register success".format(item.username))
        return {"message": "注册成功"}
    else:
        logger.error(
            "{} register failed, because username is repeat".format(item.username)
        )
        return {"message": "用户名重复，注册失败"}


# 删除用户
@usersRouter.post("/users/delete")
async def delete(item: users):
    if crud.delete_user(item.username, item.password):
        logger.info("{} delete success".format(item.username))
        return {"message": "删除成功"}
    else:
        logger.error(
            "{} delete failed, because password is wrong".format(item.username)
        )
        return {"message": "密码错误，删除失败"}


# 修改密码
@usersRouter.post("/users/update")
async def update(item: users_update):
    if crud.update_user(item.username, item.old_password, item.new_password):
        logger.info("{} update success".format(item.username))
        return {"message": "修改成功"}
    else:
        logger.error(
            "{} update failed, because password is wrong".format(item.username)
        )
        return {"message": "密码错误，修改失败"}
