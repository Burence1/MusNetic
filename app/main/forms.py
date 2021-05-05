from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):

  review_content=TextAreaField('Track review')
  submit= SubmitField('Submit')