from flask import Flask, url_for, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from search import Stalk
from models import db
from models import Number
from forms import DataForm
from sqlalchemy import exc

app = Flask(__name__)
user_data_dict = {}

db.init_app(app)

app.config["SECRET_KEY"] = "SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    form = DataForm()
    print("OH YES")
    if form.validate_on_submit():
        print("OH AGAIN")
        number_from = form.number_from.data
        number_to = form.number_to.data
        email = form.email.data

        with app.app_context():
            number = Number(email=email, number_from=number_from, number_to=number_to)
            db.session.add(number)
            db.session.commit()
            flash("Successfully sent message, wait a few minutes to recieve")

        user_data_dict[email] = Stalk(email)
        user_data_dict[email].search(email)
        user_data_dict[email].write(user_data_dict[email].results)

    return render_template("index.jinja2", form=form)

@app.route("/data")
def data():
    with app.app_context():
        numbers = Number.query.all()
    return render_template("data.jinja2", data=numbers)

@app.route("/data/<string:email>")
def user_data(email):
    with app.app_context():
        numbers = Number.query.filter_by(email=email).all()
    return render_template("data.jinja2", data=numbers)

@app.route("/data/<string:email>/search_results")
def search_results(email):
    links = []
    with open(f"{str(email)}.txt", "r") as user_data:
        user_data = eval(user_data.read())
    return render_template("user_data.jinja2", data=user_data.values())


if __name__ == '__main__':
    app.run(debug=True)