from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, I'm Viet ! Hehe ! *_*"
    #return render_template("index.html")

@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"Hello,{name}!"
