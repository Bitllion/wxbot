# wxbot-man 
基于werobot库，做了服务器端的管理端，前后端分离设计，通过网页增删改查 自定义关键词的私信消息
## 基于以下技术
后端：
- fastapi
- python
- sqlite
- jwt

前端:
- vue 
- element
## 开发进度

## 安装&& 运行

### 后端
建议先使用conda/python3 venv 创建一个虚拟环境

本项目:python = 3.9.12

#### 1.安装依赖
```
pip install -r backend/requirements.txt
```
#### 2.运行
```
cd backend
python main.py
```