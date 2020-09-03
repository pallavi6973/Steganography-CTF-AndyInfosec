from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    flag = StringField('Submit Your Flag', validators=[DataRequired()])
    submit = SubmitField('Submit')