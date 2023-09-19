# import libraries
from flask import Flask

# create an object for flask class
app = Flask(__name__)

# calling the function
@app.route("/")
# create a function
def hello():
    return "Hello World!"
# run the application
if __name__ == "__main__":
    app.run(debug=True)
