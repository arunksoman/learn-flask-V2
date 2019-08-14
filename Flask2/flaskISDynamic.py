from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name=request.args.get("name", "world"))
@app.route("/calculate")
def calculator():
    a = 3
    b = 2
    sum = a + b
    return render_template("calculator.html",a=a,b=b,sum=sum)