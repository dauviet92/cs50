from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    headline ="YOU"
    return render_template("index.html", headline=headline)
@app.route("/bye")
def bye():
    headline ="Goodbye!"
    return render_template("goodbye.html", headline=headline)
@app.route("/newyear")

def newyear():
    now = datetime.datetime.now()
    new_year = now.month==1 and now.day==1
    if new_year==True:
        new_year  = "IS"
    else:
        new_year = "IS NOT"
    newyear = new_year
    return render_template("newyear.html", newyear=new_year)
