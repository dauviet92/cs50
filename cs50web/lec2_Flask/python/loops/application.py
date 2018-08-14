from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Viet", "Trang", "Tuan", "Duong"]
    return render_template("index.html", names = names)
