#!/usr/bin/python
# -*- coding: UTF-8 -*-

# -----------------------------------------------------------
# WEB开发

# 服务端
# FastAPI 是web后端框架，用python编写
# 很多语言都能实现web后端，C/C++/JAVA/GO/PYTHON/LUA/NodeJS等
# 只要接收发送网络请求的语言都能实现web后端
# 主要接收响应消息

# 前端
# 前端是HTML+CSS+JS组成
# 前端也有一些框架：VUE/React/Angular/Ember/jQuery等
# 显示、响应用户操作
# -----------------------------------------------------------

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import datetime

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/", response_class=HTMLResponse)
async def server():
    html_file = open("./blessing/timePrint.html", 'r').read()
    return html_file

# @app.get("/")
# def read_root():
#     return {"lun": "Happy Chinese Valentine's Day"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# put method
# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/10' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "hello",
#   "price": 100,
#   "is_offer": true
# }'

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

@app.get("/blessing")
def get_blessing():
    return {"name": "lun", "blessing": "Happy Chinese Valentine's Day"}

@app.get("/study")
def read_study():
    file = open("main.py", "r")
    line = file.readline()
    file.close()
    return {"study": line}

@app.get("/time")
def get_time():
    now = datetime.datetime.now()
    return {"time": now.strftime("%Y-%m-%d %H:%M:%S")}