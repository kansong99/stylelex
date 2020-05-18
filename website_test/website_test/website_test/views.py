"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, url_for, redirect
from website_test import app
from . import module1

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

@app.route('/solution', methods = ["POST"])
def solution():
    """Renders the solution page."""
    if request.method == "POST":
        article = request.form["art"]
        soln = module1.oxfords(article)
        length = len(soln)
    return render_template(
        'solution.html',
        solution=soln,
        length=length,
        year=datetime.now().year,
        message='Your application description page.'
    )