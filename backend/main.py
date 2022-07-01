# -*- encoding: utf-8 -*-
"""
@文件        :main.py
@说明        :入口、主函数/web服务器
@时间        :2022/06/30 11:48:28
@作者        :fanyq
@版本        :1.0
"""
from uvicorn import run, config
from routers import *

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=9000, reload=True, debug=True)
