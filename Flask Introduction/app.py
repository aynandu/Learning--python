from flask import Flask, render_template

app = Flask(__name__)  # denote this file

@app.route('/')

def index():
    #return "Hello World"
    return render_template('./templete/index.html')


if __name__=="__main__":
    app.run(debug=True)

