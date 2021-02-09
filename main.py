from flask import Flask, render_template, redirect, url_for

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
    pass

if __name__ == "__main__":
    dashboard.run(debug=True)