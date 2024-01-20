# 导入Flask类和render_template函数。Flask类是创建应用的基础，而render_template函数用于渲染模板。
from flask import Flask, render_template

# 创建一个Flask应用实例。__name__是当前模块的名称，Flask使用这个参数来定位程序资源，如模板文件夹等。
app = Flask(__name__)

# 使用装饰器定义路由。装饰器是Python的高级特性之一，用于在不修改函数内容的情况下为函数添加新的功能。
# 这里@app.route('/show/info')告诉Flask，当用户访问网站的'/show/info'路径时，应该执行下面的index()函数。
@app.route("/show/info")
def index():
    # index函数使用render_template函数来渲染模板。
    # 'index.html'是模板文件的名称，这个文件应该放在应用的templates文件夹内。
    # Flask会自动查找并渲染这个文件，然后将其返回给用户的浏览器。
    return render_template("index.html")

# 这个条件判断语句检查是否是直接执行这个脚本（而不是导入它）。
# 如果是直接执行，__name__变量会被设置为'__main__'。
if __name__ == "__main__":
    # 如果是直接执行这个脚本，app.run()会启动Flask应用。
    # 这个命令会启动一个本地开发服务器，让开发者可以在本地测试他们的网站。
    # 默认情况下，服务器只在本机上可访问，运行在5000端口。
    app.run()
