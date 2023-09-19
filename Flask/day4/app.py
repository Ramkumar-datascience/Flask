from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    var = "Innomatics"
    lst = ['chicken','mutton','fish','prawns']

    dict = {'CB':300,"MB":400,"FB":350}
    return render_template("index.html",var = var,lst = lst,dict = dict)

@app.route("/dynamic",methods = ['GET','POST'])
def dynamic():
    name = request.form.get("inp1")
    city = request.form.get("inp2")
    return render_template("dynamic.html",name=name,city = city)

if __name__ == "__main__":
    app.run(debug=True)
