from . import db
from random import getrandbits
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.String(10) , primary_key = True)
    username = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    added_on = db.Column(db.DateTime)
    file_location = db.Column(db.String(300))

    def generate_user_id(self):
        return '6200%d' % getrandbits(16)
        

    def __init__(self , username ,firstname , lastname , age , sex , location):
        self.username = username
        self.user_id = self.generate_user_id()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.file_location = location
        self.added_on = datetime.now()

    def __repr__(self):
        return '<User %r %r %r %d %r>' % (self.user_id , self.firstname , self.lastname , self.age , self.sex)

