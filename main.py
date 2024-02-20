from flask import request
from flask import Flask, render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

@sample.route("/pagina") 
def pagina():
    return render_template("pagina.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
