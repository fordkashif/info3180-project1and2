from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.config['SECRET_KEY'] = 'mnIcdwVxqc80HQ0nYOtS'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://buaxjsebsacswt:_i8t_TBnHU5qRwxsDEU0ilUKjg@ec2-54-83-12-22.compute-1.amazonaws.com:5432/ddhf81amgep2s5"
db = SQLAlchemy(app)
from app import views
from app.models import User
