# 启动服务的方法
# uvicorn main:app --reload


# 本地打开网页
# 添加 allow_origins=["*"] 后，在本地打开网页，在网页中访问 http://127.0.0.1:8000 才能正常访问
# 服务端不配置跨域，就只能访问本地文件：如在本地找开网页，只能访问本地文件，不指明路径就在网页所属目录找，可指定相对路戏。
# 服务端配置跨域：能跨域访问，如访问：http://127.0.0.1:8000/time, 也可用相对路径访问 如：/time  则相对的路径是 http://127.0.0.1:8000


# 如果是访问域内的地址，尽量使相对地址；如：访问 http://127.0.0.1:8000/ ， 如果在 http://127.0.0.1:8000/ 有访问 http://127.0.0.1:8000/time，那么直接写成 /time

# 如果是配置了服务器，那么是在网络地址作为根地址，再寻找# 对应文件，如
# 如
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# 通过服务访问网页