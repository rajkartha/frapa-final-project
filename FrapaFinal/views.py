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

@app.route('/visualization')
def viz():
    """Renders the contact page."""
    return render_template(
        'viz.html',
        title='Visualization',
        year=datetime.now().year,
        message='ML Visualizations'
    )

@app.route('/team')
def team():
    """Renders the contact page."""
    return render_template(
        'team.html',
        title='Team-FRAPA',
        year=datetime.now().year,
        message='Team Info Page'
    )

@app.route('/ml')
def ml():
    """Renders the ml page."""
    return render_template(
        'ml.html',
        title='Machine Learning',
        year=datetime.now().year,
        message='ML Analysis Page'
    )

@app.route('/ihub')
def ihub():
    """Renders the ihub page."""
    return render_template(
        'ihub.html',
        title='Information Hub',
        year=datetime.now().year,
        message='ML Analysis Page'
    )