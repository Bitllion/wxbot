# -*- encoding: utf-8 -*-
"""
@文件        :__init__.py
@说明        :路由表
@时间        :2022/06/30 11:47:52
@作者        :fanyq
@版本        :1.0
"""
from fastapi import FastAPI, Request, Depends
from .hello import helloworld
from .users import usersRouter
from .message import messageRouter

# from config.settings import config
# from loguru import logger

# logger.remove()
# logger.add(config.logger_db_path, format=config.logger_format, rotation="10 MB")
app = FastAPI()


# async def logging_dependency(request: Request):
#     logger.debug(f"{request.method} {request.url}")
#     logger.debug("Params:")
#     for name, value in request.path_params.items():
#         logger.debug(f"\t{name}: {value}")
#     logger.debug("Headers:")
#     for name, value in request.headers.items():
#         logger.debug(f"\t{name}: {value}")

app.include_router(messageRouter)
app.include_router(usersRouter)
app.include_router(helloworld)
# app.include_router(usersRouter, dependencies=[Depends(logging_dependency)])
