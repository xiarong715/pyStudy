from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session   

app = Flask(__name__)
app.secret_key = 'lingling'

# https://zhuanlan.zhihu.com/p/104273184

@app.route("/")
def index():
    name = ""
    return render_template("index.html", data=name)


@app.route("/login")
def loginpage():
    return render_template("login.html")

# 默认是GET，因此需显示允许POST


@app.route("/loginProcess", methods=["POST", "GET"])
def loginprocess():
    if request.method == 'POST':
        name = request.form['nm']
        passwd = request.form['pwd']
        if name == 'xia' and passwd == '123':
            # return render_template("index.html", data=name)
            session['username'] = name
            return redirect(url_for("index"))       # 不接受传参，使用session技术传递参数到页面
        else:
            errormsg = "the username or password don't match."
            return render_template("error.html", data=errormsg) 
    else:
        errormsg = "method error."
        return render_template("error.html", data=errormsg)

# @app.route("/logoff")
# def logoffprocess():
    

@app.route("/news")
def newspage():
    content = "working hard."
    return render_template("news.html", data=content)


@app.route("/products")
def productspage():
    content = "we have to save money to buy something."
    return render_template("products.html", data=content)


@app.route("/pagesargs/<a>")
def pagesargspage(a):
    return render_template("pageargs.html", data=a)


app.run(host="0.0.0.0", port=2022, debug=True)
