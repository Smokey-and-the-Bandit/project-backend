"""
Flask endpoints.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
"""A dummy docstring."""
    return "<p>Hello, World!</p>"


@app.route('/hello')
def hello_with_name():
"""A dummy docstring."""
    return render_template('home.html')


@app.route('/namesake')
def greetings():
"""A dummy docstring."""
    return render_template('namesake.html', name=request.args['name'])
