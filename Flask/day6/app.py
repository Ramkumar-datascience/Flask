from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dynamic", methods=['GET','POST'])
def dynamic_routing():
    name = request.form.get("inp")
    if name == 'google':
        return redirect("https://www.google.com")
    elif name == "facebook":
        return redirect("https://www.facebook.com")
    elif name == "innomatics":
        return redirect("https://www.innomatics.in")
    return render_template("dynamic.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/display")
def display():
    return render_template("display.html")

@app.route("/search")
def search():
    return render_template("search.html")


if __name__=="__main__":
    app.run(debug=True)
