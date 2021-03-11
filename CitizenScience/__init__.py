from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='a5ac97b06027bd65a170f3d5409feeb5'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


from CitizenScience.main.routes import main


app.register_blueprint(main)
