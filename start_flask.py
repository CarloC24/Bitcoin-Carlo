from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/<variable>")
def anotherHello(variable):
    return f"this is the  variable : {variable}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")
