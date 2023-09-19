from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("abc.html")

@app.route("/username")
def user():
    var = "Innomatics"
    loc = "Hyderabad"
    lst = ['chiken','mutton','fish','prawn']
    dict = {'chicken':200,'mutton':500, 'fish':300}

    return render_template("user.html",name = var, location = loc,lst = lst,dict=dict)

if __name__ == "__main__":
    app.run(debug=True)
