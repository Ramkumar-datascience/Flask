#step-1 : import libraries
from flask import Flask

#step-2: create an object for Flask
app = Flask(__name__)

@app.route("/first")
def hello():
    return "<h1>Hello,Hi</h1>"

@app.route("/second")
def second():
    return "This is my second function"

@app.route("/<student>")
def user(student):
    names = ['siri','sireesha','ramesh','lakshmi']
    if student in names:
        return f"Welcome {student}!"
    else:
        return "Student does not exist"

@app.route("/login")
def login():
    return """
    <html>
      <head>
        <title></title>
      </head>
      <body>
        <center><h1 style="color:green"><u>Login</u></h1><br>
        Username : <input type="text" placeholder="enter username"><br><br>
        Password : <input type="password" placeholder="enter password"><br><br>
        <input type="submit" value="Login">
        </center>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
