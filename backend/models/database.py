# -*- encoding: utf-8 -*-
"""
@文件        :database.py
@说明        :数据库配置(sqlite)
@时间        :2022/06/30 11:24:31
@作者        :fanyq
@版本        :1.0
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# 创建连接
# 默认建立的对象只能让建立该对象的线程使用，check_same_thread设置为False可以让多个线程同时使用
# 默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印
engine = create_engine("sqlite:///wx.db?check_same_thread=False", echo=False)
# 创建基本映射类
Base = declarative_base()

# 定义映射类user
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))

    # __repr__方法用于print该类的对象时，显示的字符串
    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)


# 定义映射类message
class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    keyword = Column(String(100))
    message = Column(String(1000))


# 映射类到数据库
Base.metadata.create_all(bind=engine)
