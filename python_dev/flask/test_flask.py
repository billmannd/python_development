# -*- coding: utf-8 -*-
"""
Test Flask Application

Author: Dan Billmann

"""
from flask import Flask, request, render_template#, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=name)

@app.route("/login", methods = ["GET","POST"])
@app.route("/login/<name>")
def login(name=None):
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            username = request.form['username']
            return "Yay! %s" % username
        else:
            error = "Invalid username or password"
    
    return render_template("login.html", error=error)


@app.route("/user/<string:username>")
def profile(username):
    return "User %s" % username

@app.route("/post:<int:post_id>")
def post(post_id):
    return "Post %d" % post_id

"""
#print(url_for("index"))
#print(url_for("login"))
#print(url_for("login", next= "/"))
#print(url_for("profile", username = "Willian"))
"""

with app.test_request_context('/hello', method='POST'):
    # now you can do something to this request until
    # the end of the with block
    assert request.path == "/hello"
    assert request.method == "POST"
    