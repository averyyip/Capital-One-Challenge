from app import app
from flask import render_template, flash, redirect, request
from estimates import *

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", estimate_price="", estimate_weekly_revenue="", scroll=None)

@app.route('/handle_rev', methods=['POST'])
def handle_rev():
    lat = request.form['lat']
    lon = request.form['lon']
    rev = "$" + str(round(estimate_weekly_rev(lat,lon), 2))
    return render_template("index.html", estimate_price="", estimate_weekly_revenue=rev, scroll="rev")

@app.route('/handle_price', methods=['POST'])
def handle_price():
    lat = request.form['lat']
    lon = request.form['lon']
    price = "$" + str(round(estimate_ideal_price(lat,lon), 2))
    return render_template("index.html", estimate_price=price, estimate_weekly_revenue="", scroll="price")

@app.route("/favicon.ico")
def favicon():
    return(url_for('static',filename='favicon.ico')
