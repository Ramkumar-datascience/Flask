import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

###################### Database Configuration ########################
basedir = os.path.abspath(os.path.dirname(__file__))
#basedir = "C:\Users\DELL\OneDrive\Desktop\batch_164_168_174\Database"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
######################################################################
############Model Creation ###########################################
class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return "Item Name - {} and Price - {}".format(self.name, self.price)
######################################################################

@app.route("/")
def index():
    return "Hello"

@app.route("/add", methods=['GET','POST'])
def insert():
    name = request.form.get('item_name')
    price = request.form.get('item_price')
    data = Hotel(name,price)

    db.session.add(data)
    db.session.commit()
    print(name, price)
    return render_template("add.html")

@app.route("/display")
def display():
    info = Hotel.query.all()
    return render_template("display.html",info=info)

if __name__=="__main__":
    app.run(debug=True)
