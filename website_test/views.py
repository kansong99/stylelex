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

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
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

@app.route('/product')
def product():
    """Renders the product page."""
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
dict = {'yes': True, 'no': False}

@app.route('/solution', methods = ["POST"])
def solution():
    """Renders the solution page."""
    if request.method == "POST":
        article = request.form["art"]
        llist = LinkedList(article)
        #if request.form["oxfords"] == "no":
        #    find_func(False, llist)
        #elif request.form["oxfords"] == "yes":
        #    find_func(True, llist)
        #else:
        #    pass
        #names_func(True, True, True, llist)
        #dict[request.form["oxfords"]]
        names_func(llist, option1 = dict[request.form["names1"]], option2 = dict[request.form["names2"]], option3 = dict[request.form["names3"]])
        numb_func(llist, dict[request.form["numbers1"]], dict[request.form["numbers2"]], dict[request.form["numbers3"]], dict[request.form["numbers4"]], dict[request.form["numbers5"]], dict[request.form["numbers6"]])
        solution = llist.tostring()
        jsolution = llist.toarray()
        length = len(solution)
        check = json.dumps(jsolution)
        print(check)
    return render_template(
        'solution.html',
        parsed=jsolution,
        solution=solution,
        perrors=perrors)
