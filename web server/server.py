from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, nandu great going "

@app.route("/blog")
def blog():
    return "These are my thoughts about blog "

@app.route("/temp")
def templates():
    return render_template('index.html')
@app.route("/about.html")
def about():
    return render_template('about.html')
@app.route("/<username>")
def user(username=None):
    return render_template('index.html',name=username)

'''
on terminal
$env:FLASK_APP ="server.py"
 $env:FLASK_ENV = "development"   (Ocationally used)
flask run
'''


