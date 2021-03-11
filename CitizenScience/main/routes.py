
from flask import Blueprint, render_template, url_for 
from CitizenScience import app


main=Blueprint('main', __name__)

@main.route('/home')
def homepage():
    
    return render_template('home.html')


