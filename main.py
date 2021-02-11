from flask import Flask, render_template, redirect, url_for, request
import dbfunctions


dashboard = Flask("__name__")


@dashboard.route("/")  # this sets the route to this page
def index():
    return render_template("index.html")


@dashboard.route("/home/")
def home():
    return redirect(url_for("index"))


@dashboard.route("/<content>/")
def page(content):
    return render_template("404.html", content=content.capitalize())


@dashboard.route("/dashboard/")
def dash():
    conn = dbfunctions.createConnection("testDB")
    rows = dbfunctions.getData(conn)
    conn.close()
    rows = tuple(rows)
    return render_template("dashboard.html", rows=rows)


@dashboard.route("/edit", methods=['GET', 'POST'])
def update():
    # username = request.args.get('username')
    sub = str(request.form)
    print(sub)
    print(request.method)
    # if request.method == 'POST':
    #     print(request.method)
    #     sub = request.form.get('sub-level', 0)
    # print(f"{username} {sub}")
    # conn = dbfunctions.createConnection("testDB")
    # dbfunctions.updateSubLevel(conn, [sub, username])
    # conn.close()
    return redirect(url_for("dash"))


if __name__ == "__main__":
    dashboard.run(debug=True)
