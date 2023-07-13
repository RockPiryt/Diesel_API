#top_cars forms

#--------------------------------Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


##------------------------------Editform to add img to database
class EditForm(FlaskForm):
    img_source = StringField(label="Please paste url to car image", validators=[DataRequired()])
    submit = SubmitField(label="Update")

class AddCarForm(FlaskForm):
    make = StringField(label="Please give make", validators=[DataRequired()])
    model = StringField(label="Please give model", validators=[DataRequired()])
    year = IntegerField(label="Please give year", validators=[DataRequired()])
    engine = FloatField(label="Please give engine", validators=[DataRequired()])
    fuel = StringField(label="Please give fuel", validators=[DataRequired()])
    transmission = StringField(label="Please give transmission", validators=[DataRequired()])
    size = StringField(label="Please give size", validators=[DataRequired()])
    consumption = FloatField(label="Please give consumption", validators=[DataRequired()])
    img_source = StringField(label="Please paste url to car image", validators=[DataRequired()])
    submit = SubmitField(label="Update")