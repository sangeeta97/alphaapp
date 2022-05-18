from flask import render_template, redirect, url_for, flash, request, current_app
from flask_wtf.file import FileAllowed, FileRequired
from flask import Flask, send_from_directory, render_template, request, redirect, url_for, g, flash
from .forms import ItemForm
from flask_login import login_user, logout_user, login_required, current_user
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from wtforms.widgets import Input
from werkzeug.utils import secure_filename, escape, unescape
from markupsafe import Markup
import pdb
import sqlite3
import datetime
from secrets import token_hex
import os
from sqlalchemy import update
from flask import jsonify
import numpy as np
import pandas as pd
from flask import send_file, send_from_directory, safe_join, abort
from . import alpha
from ..model import User
from .. import db
# top_package = __import__(__name__.split('.')[0])
# import f'{top_package}'.model.User as User
# import top_package.run.db as db

context= {'extra': False}



def randomString():
        ALPHABET = np.array(list('abcdefghijklmnopqrstuvwxyz0123456789'))
        stringArray = np.random.choice(ALPHABET, size=10)
        outString = ""
        return outString.join(stringArray)




@alpha.route('/alpha', methods=['POST', 'GET'])
@alpha.route('/alpha/home', methods=['POST', 'GET'])
def home_page():
    form = ItemForm()
    if form.validate_on_submit():
        name1 = request.form['name']
        email = request.form['email']
        param_model = request.form['param_model'] if request.form['param_model'] else 'monomer'
        param_db = request.form['param_db'] if request.form['param_db'] else 'full_dbs'
        file = request.files['inputfile']
        filename1 = secure_filename(file.filename)
        filename11= filename1.split(".")[0]
        filename22= filename1.split(".")[-1]
        uniquestr1 = randomString()
        filename1= f'{filename11}_{uniquestr1}' + "." + filename22
        filename2= f'{filename11}_{uniquestr1}'
        state = False
        file.save(os.path.join(current_app.config["static"], "input", filename1))

        record = User(name1, email, param_model, param_db, filename1, filename2, uniquestr1, state)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()

        message = flash(f"The data for user {name1} for analysis has been submitted.")
        return render_template('alpha_last.html', message=message, uniquestr= uniquestr1)
    if form.errors:
        flash("{}".format(form.errors), "danger")

    return render_template('alpha_first.html', form= form)


@alpha.route('/alpha/download/<string:uniquestr>')
def download_page(uniquestr):
    trick = User.query.filter_by(uniquestr=uniquestr).all()
    outputfile= [u.outputfile for u in trick]
    filename= outputfile[0]
    filename= filename + ".zip"
    return send_file(os.path.join(current_app.config["static"], "output", filename),
                            as_attachment=True)





@alpha.route('/alpha/upload', methods=['PUT', 'POST'])
def upload():
    if request.files['filedata']:
        file= request.files['filedata']
        filename=secure_filename(file.filename)
        file.save(os.path.join(current_app.config["static"], "output", filename))
        filename= filename.split(".")[0]
        trick = User.query.filter_by(outputfile=filename).all()
        id= [u.id for u in trick]
        id= id[0]
        user = User.query.get(int(id))
        if user:
            user.name= user.name
            user.email= user.email
            user.param_model= user.param_model
            user.param_db= user.param_db
            user.inputfile= user.inputfile
            user.outputfile= user.outputfile
            user.uniquestr= user.uniquestr
            user.state= True
            db.session.commit()
    return "success"


@alpha.route('/alpha/database')
def database():
    trick = User.query.filter_by(state=False).all()
    email= [u.email for u in trick]
    param_model= [u.param_model for u in trick]
    param_db= [u.param_db for u in trick]
    inputfile= [u.inputfile for u in trick]
    outputfile= [u.outputfile for u in trick]
    state = [u.state for u in trick]
    uniquestr= [u.uniquestr for u in trick]
    name= [u.name for u in trick]
    table= {"email": email, "name": name, "param_model": param_model, "param_db":param_db, "inputfile": inputfile, "outputfile": outputfile, "uniquestr": uniquestr, "state": state}
    return jsonify(table)
