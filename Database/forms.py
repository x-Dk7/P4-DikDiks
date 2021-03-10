from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddForm(FlaskForm):
    p_name = StringField('name of character')
    p_date = StringField('date of creation')
    submit = SubmitField('add character')
