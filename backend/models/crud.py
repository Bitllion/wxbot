# -*- encoding: utf-8 -*-
"""
@文件        :crud.py
@说明        :数据库增删改查
@时间        :2022/06/30 11:26:32
@作者        :fanyq
@版本        :1.0
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import *

engine = create_engine("sqlite:///wx.db?check_same_thread=False", echo=False)
Base = declarative_base()

# 删除message
def delete_message(username: str, keyword: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Message)
    # 判断
    if query_message(username):
        message_obj = query.filter(Message.username == username).all()
        for message in message_obj:
            if message.keyword == keyword:
                session.delete(message)
        session.commit()
        session.close()
        return True
    else:
        return False


# 修改message
def update_message(username: str, keyword: str, message: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Message)
    # 判断
    if query_message(username):
        message_obj = query.filter(Message.username == username).all()
        for i in message_obj:
            if i.keyword == keyword:
                i.message = message
        session.commit()
        session.close()
        return True
    else:
        return False


# 查询message
def query_message(username: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Message)
    message_obj = query.filter(Message.username == username).all()
    message_list = []
    for message in message_obj:
        message_dict = {}
        message_dict["id"] = message.id
        message_dict["username"] = message.username
        message_dict["keyword"] = message.keyword
        message_dict["message"] = message.message
        message_list.append(message_dict)
    return message_list


# 添加message
def add_message(username: str, keyword: str, message: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    # 判断keyword是否存在
    message_list = query_message(username)
    if message_list:
        for i in message_list:
            if i["keyword"] == keyword:
                return False
        # 创建message对象
        message = Message(username=username, keyword=keyword, message=message)
        # 添加到session
        session.add(message)
        # 提交到数据库
        session.commit()
        # 关闭session
        session.close()
        return True
    else:
        # 创建message对象
        message = Message(username=username, keyword=keyword, message=message)
        # 添加到session
        session.add(message)
        # 提交到数据库
        session.commit()
        # 关闭session
        session.close()
        return True


# 添加用户
def add_user(username: str, password: str):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # 判断
    if query_user(username):
        return False
    else:
        # 创建user对象
        user = User(username=username, password=password)
        # 添加到session
        session.add(user)
        # 提交到数据库
        session.commit()
        # 关闭session
        session.close()
        return True


# 查询用户密码字典
def query_user(username: str):
    # 创建Session连接
    Session = sessionmaker(bind=engine)
    # 创建Session对象
    session = Session()
    # 创建user表查询对象query
    query = session.query(User)
    # 查询name为name的对象
    user_obj = query.filter(User.username == username).all()
    # 关闭Session连接
    session.close()
    # 返回查询结果字典
    user_dict = {}
    for user in user_obj:
        user_dict["id"] = user.id
        user_dict["username"] = user.username
        user_dict["password"] = user.password
    return user_dict


# 删除用户
def delete_user(username: str, password: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(User)
    # 判断
    if query_user(username):
        if query_user(username)["password"] == password:
            user_obj = query.filter(User.username == username).all()
            for user in user_obj:
                session.delete(user)
            session.commit()
            session.close()
            return True
        else:
            return False
    else:
        return False


# 修改密码
def update_user(username: str, old_password: str, new_password: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(User)
    # 判断
    if query_user(username):
        if query_user(username)["password"] == old_password:
            user_obj = query.filter(User.username == username).all()
            for user in user_obj:
                user.password = new_password
            session.commit()
            session.close()
            return True
        else:
            return False
    else:
        return False
