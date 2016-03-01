import json
from app import app
from flask import url_for, redirect, render_template, request , flash, jsonify, Response
from app.forms import UserForm
from app import db
from app.models import User
import os
from random import getrandbits

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/profile' , methods=['GET' , 'POST'])
def profile():
    form = UserForm()
    
    if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        users = db.session.query(User).all()
        return user_list_json(users)
    if request.method == 'GET':
        return render_template('new.html', form=form)
    elif form.validate():
        fname = form.fname.data
        lname = form.lame.data
        uname = form.uname.data
        sex = form.sex.data
        age = form.age.data
        img = form.img.data
        user = User(uname ,fname , lname ,  age , sex ,'')
        file = str(getrandbits(20)) + img.file
        img.save(os.path.join("app/static", file))
        user.file_location = file
        db.session.add(user)
        db.session.commit()
        flash('Created')
        return redirect(url_for('preview' , user_id=user.user_id))
    else:
        return render_template('profile.html' , form=form,errors=form.errors.items())

@app.route('/profiles')
def index():
    users = db.session.query(User).all()
    if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        return user_list_json(users)
        
    if len(users) == 0:
        return 'No Registered Users'
    return render_template('index.html' , users=users)


@app.route('/profile/<user_id>' , methods=['GET' , 'POST'])
def preview(user_id):
    user = db.session.query(User).filter_by(user_id=user_id).first()
    if user == None:
        if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
            return jsonify(message="Resource not found") , 404
        return render_template('404.html'), 404
    date = format_date(user.added_on)
    if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        return jsonify(userid=user.user_id , username=user.username , image=user.file_location , age=user.age , profile_added_on=date)
    return render_template('preview.html', user=user , date=date)

@app.errorhandler(404)
def page_not_found(e):
    if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        return jsonify(message="Resource not found") , 404
    return render_template('404.html'), 404


def format_date(date):
    return date.strftime('%a %W %b %Y')

def user_list_json(users):
    user_json = []
    for user in users:
        user_json.append({'username': user.username , 'userid': user.user_id})
    return Response(json.dumps(user_json) , mimetype='application/json')

