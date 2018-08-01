from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import SelectField, Form, BooleanField, StringField, PasswordField, IntegerField, TextAreaField, TextField, SubmitField, RadioField
from wtforms import validators, ValidationError
from bson.objectid import ObjectId #for accesing objectid in mongodb
import numpy as np
import itertools
from collections import Counter, defaultdict


def connect():
    connection = MongoClient('127.0.0.1', 27017)
    handle = connection["projectfinder"]
    return handle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
handle = connect()


class ContactForm(Form):
    name = TextField("Name of Student", [validators.Required("Please Enter Your Name")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")
    email = TextField("Email", [validators.Required("Please enter your Email Address"), validators.Email("Please enter your Email Address")])
    age = IntegerField('Age')
    language = SelectField("Languages", choices=[('JV', 'Java'), ('PY', 'Python')] )
    submit = SubmitField("Send")

class LanguagesSelection(FlaskForm):
    language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    location = SelectField('Location', choices=[('Köln', 'Köln'), ('Bonn', 'Bonn'), ('Leipzig', 'Leipzig'), ('Frankfurt', 'Frankfurt'), ('Hamburg', 'Hamburg')])
    langD = SelectField('Language', choices=[])

@app.route('/', methods= ['GET', 'POST'])
def index():
    form = LanguagesSelection()
    lang = form.language.data
    loc = form.location.data
    return render_template('index.html', form=form)

@app.route('/home', methods= ['GET', 'POST'])
def home():
    form = LanguagesSelection()
    loc = form.location.data
    lang = form.langD.data
    #cat = form.location.data
    #db = handle.itproject.({})
    if loc == "None":
        loc = 'Köln'
    db = handle.itproject.find({"location":loc})
    print(loc)
    #print(cat)
    a = []
    for x in db:
        b = x['skills']
        a.append(b)
    merged = list(itertools.chain.from_iterable(a))
    cleaned = set(merged)
    final_cleaned = list(cleaned)
    if 'None' in final_cleaned:
        final_cleaned.remove('None')
    final_cleaned.sort()

    print(len(merged))
    print(len(final_cleaned))
    #print(final_cleaned)
    #print(e)
    #print(c)
    #for a in c:
        #print(a)

    print(db.count())

    form.langD.choices = [(city, city[:20]) for city in final_cleaned]
    if request.method == 'POST':
        #returns the objectid of the selected city
        #finds the city which has the objid
        print(lang)
        skills = handle.itproject.find({"skills" : lang})[0]
        #print(skills)
        #city = City.query.filter_by(id=form.city.data).first()
        return '<h1>Location: {}, Skills: {}</h1>'.format(loc, skills['skills'][:4])
    return render_template('home.html', form=form)
    #form.langD.choices = [(city['skills'][:], city['skills'][:]) for city in db]
    #form.city.choices = [(city['_id'], city['skills']) for city in db]

    #return render_template('home.html', form=form)
    #return render_template('home.html', form=form)

@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate == False:
            return render_template('contact.html', form=form)
        else:
            flash('Your account has been created! You are now able to log in', 'success')
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)






if __name__ == '__main__':
    app.run(debug=True)
