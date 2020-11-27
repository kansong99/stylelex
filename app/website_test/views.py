"""
Routes and views for the flask application.
"""
import json

from datetime import datetime
from flask import render_template, request, url_for, redirect, Flask
from website_test import app
from .links import *
from .find3 import *
from .names3 import *
from .numb import *
#converts yes to True and no to False
dict = {'yes': True, 'no': False}
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    url = url_for('static', filename='App.js')
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        bundle = url
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='about',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/product', methods=["GET", "POST"])
def product():
    """Renders the product page."""
    if request.method == "POST":
        article = request.form["art"]
        llist = LinkedList(article)
        names_func(llist, dict[request.form["names1"]], dict[request.form["names2"]], dict[request.form["names3"]])
        numb_func(llist, dict[request.form["numbers1"]], dict[request.form["numbers2"]], dict[request.form["numbers3"]], dict[request.form["numbers4"]], dict[request.form["numbers5"]], dict[request.form["numbers6"]])
        jsolution = llist.toarray()
        #check = json.dumps(jsolution)
        return render_template(
            'solution.html',
            solution = article,
            jsolution = jsolution
        )
        #return redirect(url_for('solution', text=text))
    return render_template(
        'product.html',
         title='about',
         year=datetime.now().year,
         message='Your application description page.'
    )

#@app.route('/solution', methods = ["POST"])
#def solution():
#    """Renders the solution page."""
#    if request.method == "POST":
#        article = request.form["art"]
#        if request.form["oxfords"] == "no":
#            solution = module1.oxfords(article, False)
#            msg = "Remove Oxford comma at position -" 
#        else:
#            request.form["oxfords"] == "yes"
#            solution = module1.oxfords(article, True)
#            msg = "Oxford comma expected at position -"
#        length = len(solution)
#        words = len(article)
#    return render_template(
#        'solution.html',
#        solution=solution,
#        length=length,
#        article=article,
#        words=words,
#        year=datetime.now().year,
#        message=msg
#    )
#converts yes to True and no to False

#@app.route('/solution', methods = ["POST"])
@app.route('/solution/<string:text>')
def solution(text):
    """Renders the solution page."""
    return f'{text}'

    #if request.method == "POST":
       # article = request.form["art"]
       # llist = LinkedList(article)
       
       # names_func(llist, option1 = dict[request.form["names1"]], option2 = dict[request.form["names2"]], option3 = dict[request.form["names3"]])
       # numb_func(llist, dict[request.form["numbers1"]], dict[request.form["numbers2"]], dict[request.form["numbers3"]], dict[request.form["numbers4"]], dict[request.form["numbers5"]], dict[request.form["numbers6"]])
       # solution = llist.tostring()
       # jsolution = llist.toarray()
       # check = json.dumps(jsolution)
    #return render_template(
    #    'solution.html')
