"""
Flask endpoints.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    high level support for doing this and that.
    """
    return '<p>Hello, World!</p>'


@app.route('/hello')
def hello_with_name():
    """
    high level support for doing this and that.
    """
    return render_template('home.html')


@app.route('/namesake')
def greetings():
    """
    high level support for doing this and that.
    """
    return render_template('namesake.html', name=request.args['name'])
