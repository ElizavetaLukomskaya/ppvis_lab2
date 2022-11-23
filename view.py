import psycopg2
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (jsonify, request)
import pandas as pd

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/attract')
def attract_page():
    return render_template('attract.html')

@app.route('/info_cachel')
def info_cachel_page():
    return render_template('info_cachel.html')

@app.route('/info_carousel')
def info_carousel_page():
    return render_template('info_carousel.html')

@app.route('/info_coleso')
def info_coleso_page():
    return render_template('info_coleso.html')

@app.route('/ticket')
def ticket_page():
    return render_template('ticket.html')

@app.route('/ticket_list')
def ticket_list_page():
    return render_template('ticket_list.html')

@app.route('/ticket_buy')
def ticket_buy_page():
    return render_template('ticket_buy.html')

@app.route('/shop')
def shop_page():
    return render_template('shop.html')

@app.route('/shop_list')
def shop_list_page():
    return render_template('shop_list.html')

@app.route('/shop_buy')
def shop_buy_page():
    return render_template('shop_buy.html')