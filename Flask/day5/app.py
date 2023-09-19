from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/login",methods=['GET','POST'])
def login():
    database = {'siri':2020, 'ashok':2021,"kaasi":2022}
    username = request.form.get('uname')
    password = request.form.get("pwd")
    if username in database:
        if database[username]==int(password):
            return render_template("success.html",username=username)
        else:
            return render_template("fail.html")
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
