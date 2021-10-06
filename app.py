from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/submit", methods=['GET','POST'])
def submit():
    database = {'ram':'1234'}
    name = request.form.get('name')
    pwd = request.form.get('password')
    if name in database.keys():
        if pwd == database[name]:
            print("im here")
            return render_template('index.html',name = name)
    return render_template('index.html')
    
@app.route("/", methods=['GET','POST'])
def hello():
   
    if request.method == 'POST':
        lst = [1,2,3,4]
        name1 = request.form.get('name')
        return render_template("index.html",lst = lst, name1=name1)
    return render_template("index.html")
    
@app.errorhandler(404)
def pagenotfound(e):
    return "Wrong URL"

if __name__ == '__main__':
    app.run(debug=True)