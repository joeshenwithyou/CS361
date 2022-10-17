from flask import Blueprint, \
    render_template, request, jsonify, redirect, url_for, \
    flash
from datetime import datetime

views = Blueprint(__name__, "views")

@views.route("/")
def homepage():
	return render_template("index.html")

@views.route("/home")
def home():
	return render_template("homepage.html")

@views.route("/card-database")
def card_database():
	return render_template("card_database.html")

@views.route("/my-cards")
def my_cards():
	return render_template("my_cards.html")

@views.route("/help")
def help():
	return render_template("help.html")

@views.context_processor
def inject_now():
    return {'now': datetime.utcnow()}