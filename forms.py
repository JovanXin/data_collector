from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import TelField


class DataForm(FlaskForm):
    """ 
    A form that allows users to enter personal information
    """
    number_from = StringField("Number from", [DataRequired(), Length(min=6, max=12)])
    number_to = StringField("Number to", [DataRequired()])
    email = StringField("Your email", [Email(), DataRequired(), Length(max=50)])
    submit = SubmitField("Send")
