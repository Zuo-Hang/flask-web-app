# encoding : utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    title = 'flask web app'
    paragraph = [
        'p1',
        'p2',
        'p3'
    ]
    # 传递变量
    return render_template('index.html', title=title, paragraph=paragraph)


if __name__ == '__main__':
    # 热加载、端口号、主机号（其他机器可访问）
    app.run(debug=True, port=3000, host='0.0.0.0')
