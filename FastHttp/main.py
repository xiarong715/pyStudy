from urllib import response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles

import datetime

app = FastAPI()

# 加载静态文件
app.mount("/cs", StaticFiles(directory="blessing/css"), "cs")
app.mount("/js", StaticFiles(directory="blessing/js"), "js")

# 添加 allow_origins=["*"] 后，本地打开网页，在网页中访问 http://127.0.0.1:8000 才能正常访问
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/", response_class=HTMLResponse)
def get_root():
    html_file = open("./blessing/index.html", "r").read()
    return html_file

@app.get("/blessing")       # 默认返回的类型是Json类型的数据
def get_blessing():
    return {"name": "Lun", "blessing": "Happy Chinese Valentine's day"}

@app.get("/time")
def get_time():
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": now_time}

# load static resource
# @app.get("/style.css", response_class=PlainTextResponse)
# def get_style():
#     style_file = open("./blessing/css/style.css", "r").read()
#     return style_file

# @app.get("/jquery.min.js", response_class=PlainTextResponse)
# def get_jquery():
#     jquery_file = open("./blessing/js/jquery.min.js", "r").read()
#     return jquery_file

# @app.get("/script.js", response_class=HTMLResponse)
# def get_script():
#     js_file = open("./blessing/js/script.js", "r").read()
#     return js_file


