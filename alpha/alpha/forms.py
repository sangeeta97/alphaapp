from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,HiddenField, IntegerField
from wtforms.validators import EqualTo, Length,Email,DataRequired, ValidationError
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from wtforms.widgets import Input
from werkzeug.utils import secure_filename, escape, unescape
from markupsafe import Markup
import pdb
import sqlite3
from wtforms import FileField, StringField, TextAreaField, SubmitField, SelectField, DecimalField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from wtforms.widgets import Input
from flask_wtf.file import FileAllowed, FileRequired
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired , Email , Length



class ItemForm(FlaskForm):
    name = StringField("name", validators=[InputRequired("Input is required!"), DataRequired("Data is required!")])
    email = StringField('Email', validators=[DataRequired("Data is required!"), Email(message="Invalid Id , Check the Format")])
    param_model = SelectField('Choose the model type',
        choices=[ ('', ''), ('monomer_model', 'monomer_model'),
        ('multimer_model', 'multimer_model')])
    param_db= SelectField('Choose the database type',
        choices=[ ('', ''), ('reduced_dbs', 'reduced_dbs'),
        ('full_dbs', 'full_dbs')])
    inputfile = FileField(validators=[InputRequired("Input is required!")])

    submit=SubmitField(label='Submit Analysis')
