from flask import Flask, render_template, redirect, url_for, request
from flask.globals import session
import dbfunctions
import random
import string
import os

dashboard = Flask("__name__")
application = dashboard
dashboard.secret_key = ''.join(random.choices(string.ascii_uppercase + string.ascii_letters +
                                              string.ascii_lowercase + string.punctuation + string.digits, k=16))
# databaseLocation = os.getenv("DATABASE")


@dashboard.route("/")  # this sets the route to this page
def index():
    return render_template("index.html")


@dashboard.route("/home/")
def home():
    return redirect(url_for("index"))


@dashboard.route("/features/")
def features():
    return render_template("features.html")


@dashboard.route("/pricing/")
def pricing():
    return render_template("pricing.html")


@dashboard.route("/<content>/")
def error(content):
    return render_template("404.html", content=content.capitalize())


@dashboard.route("/dashboard/")
def dash():
    if session.get("username") == "admin" and session.get("password") == "testing":
        print("success")       
        conn = dbfunctions.createConnection("testDB")
        rows = dbfunctions.getData(conn)
        conn.close()
        rows = tuple(rows)
        return render_template("dashboard.html", rows=rows)
    else:
        return redirect(url_for("login"))


@dashboard.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["usernameInput"]
        password = request.form["passwordInput"]
        session["username"] = username
        session["password"] = password
        return redirect(url_for("dash"))
    else:
        return render_template("login.html")


@dashboard.route("/edit", methods=['GET', 'POST'])
def update():
    req = ""
    if request.method == 'POST':
        req = request.form.get('sub-level', 0).split("[{(..++--**//)}]")

    username = req[0]
    sub = int(req[1])
    conn = dbfunctions.createConnection("testDB")
    dbfunctions.updateSubLevel(conn, [sub, username])
    conn.close()
    return redirect(url_for("dash"))


if __name__ == "__main__":
    dashboard.run()
