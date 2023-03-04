from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello')
def hello_with_name():
    return render_template('home.html')


@app.route('/namesake')
def greetings():
    return render_template('namesake.html', name=request.args['name'])
