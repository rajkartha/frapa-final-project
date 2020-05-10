"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FrapaFinal import app

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

@app.route('/plot')
def plot():
    """Renders the contact page."""
    return render_template(
        'plot.html',
        title='Financial Report',
        year=datetime.now().year,
        message='Your Financial report page.'
    )

@app.route('/about')
def about():
    """Renders the ml page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='ML Analysis Page'
    )
