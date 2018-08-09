from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import SelectField, Form, BooleanField, StringField, PasswordField, IntegerField, TextAreaField, TextField, SubmitField, RadioField
from wtforms import validators, ValidationError
from bson.objectid import ObjectId #for accesing objectid in mongodb
#import numpy as np
#import pandas as pd
import itertools
from collections import Counter, defaultdict
from string import punctuation
import re



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
    location = SelectField('Location', choices=[])
    #location = SelectField('Location', choices=[('Köln', 'Köln'), ('Bonn', 'Bonn'), ('Leipzig', 'Leipzig'), ('Frankfurt', 'Frankfurt'), ('Hamburg', 'Hamburg')])
    langD = SelectField('Language', choices=[])
    skill = SelectField('City', choices=[])

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
        loc = 'Leipzig'
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
    #locate = handle.itproject.find
    l = handle.itproject.find({})
    #list = [''.join(c for c in s if c not in punctuation) for s in list]

    clean_list = []
    for data in l:
        #pattern = re.compile(r"\d+")
        #pattern2 = re.compile(r"\s")
        result = data['location']
        #y = pattern.sub("", result)


        clean_list.append(result)

    cleaned = set(clean_list)

    final_cleaned2 = list(cleaned)

    final_cleaned2 = [x for x in final_cleaned2 if not ('Nor' in x or 'D-' in x or 'Nähe' in x or 'PLZ' in x or '[^A-Za-z0-9]' in x )]


    final_cleaned2.sort()
    #final = final_cleaned
    #final_cleaned = [''.join(c for c in s if c not in punctuation) for s in final_cleaned]
    print(len(final_cleaned2))
    #print(fa)
from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import SelectField, Form, BooleanField, StringField, PasswordField, IntegerField, TextAreaField, TextField, SubmitField, RadioField
from wtforms import validators, ValidationError
from bson.objectid import ObjectId #for accesing objectid in mongodb
#import numpy as np
#import pandas as pd
import itertools
from collections import Counter, defaultdict
from string import punctuation
import re



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
    location = SelectField('Location', choices=[])
    #location = SelectField('Location', choices=[('Köln', 'Köln'), ('Bonn', 'Bonn'), ('Leipzig', 'Leipzig'), ('Frankfurt', 'Frankfurt'), ('Hamburg', 'Hamburg')])
    langD = SelectField('Language', choices=[])
    skill = SelectField('City', choices=[])

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
        loc = 'Amberg'
    #loc = form.location.data
    db = handle.good.find({"region": loc})
    """final = []
    for data in db:
        final.append(data["location"])


    print(len(final))
    a = db.count()
    print(db)
    #print(len(final))
    print(a)
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
    #locate = handle.itproject.find"""
    l = handle.good.find()
    #print(l)

    #list = [''.join(c for c in s if c not in punctuation) for s in list]

    clean_list = []
    for data in l:
        #pattern = re.compile(r"\d+")
        #pattern2 = re.compile(r"\s")
        result = data['region']
        #y = pattern.sub("", result)


        clean_list.append(result)

    cleaned = set(clean_list)

    final_cleaned2 = list(cleaned)

    #final_cleaned2 = [x for x in final_cleaned2 if not ('Nor' in x or 'D-' in x or 'Nähe' in x or 'PLZ' in x or '[^A-Za-z0-9]' in x )]


    final_cleaned2.sort()
    #final = final_cleaned
    #final_cleaned = [''.join(c for c in s if c not in punctuation) for s in final_cleaned]
    print(len(final_cleaned2))
    #print(fa)

    #print(l)
    #print(db.count()
    Region = handle.good.distinct("region")
    Skills = handle.good.find({"location": loc})

    Region.sort()
    form.location.choices = [(city[:], (city[:]))for city in Region ]
    form.skill.choices = [(city["_id"], city["skills"][0])for city in Skills]
    print(loc)

    #form.langD.choices = [(city, city[:20]) for city in final_cleaned]
    if request.method == 'POST':
        #returns the objectid of the selected city
        #finds the city which has the objid
        print(lang)
        skills = handle.good.find({"skills" : lang})[0]
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

@app.route('/home/<location>')
def city(location):
    #get cities given by the user
    stadt = handle.good.find({"location":location})
    cityArray = []
    for city in stadt:
        cityObj = {}
        city['skills']
        obj_id = str(city["_id"]) #objid cant be jsonified so we cob´nvert to string
        cityObj['id'] = obj_id
        cityObj['location'] = city['location'][0]
        cityObj['skills'] = city['skills'][0][:20]
        cityArray.append(cityObj)
        #print(obj_id)

    return jsonify({'stadt' : cityArray})

@app.route('/test')
def test():
    hey = handle.itproject.find({"location":{"$regex": "/^.*Frankfurt*/"}})
    print(hey.count())



if __name__ == '__main__':
    app.run(debug=True)

    #print(l)
    print(db.count())
    form.location.choices = [(city[:20], city[:20]) for city in final_cleaned2]
    form.skill.choices = [(city["_id"], list(set(city["skills"]))[0])for city in handle.itproject.find({"location": loc})]
    print(loc)

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

@app.route('/home/<location>')
def city(location):
    #get cities given by the user
    stadt = handle.itproject.find({"location":location})
    cityArray = []
    for city in stadt:
        cityObj = {}
        city['skills']
        obj_id = str(city["_id"]) #objid cant be jsonified so we cob´nvert to string
        cityObj['id'] = obj_id
        cityObj['location'] = city['location'][0]
        cityObj['skills'] = city['skills'][0][:20]
        cityArray.append(cityObj)
        #print(obj_id)

    return jsonify({'stadt' : cityArray})




if __name__ == '__main__':
    app.run(debug=True)
