from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

##------------------------------Flaskforms
class EditForm(FlaskForm):
    img_source = StringField(label="Please paste url to car image", validators=[DataRequired()])
    submit = SubmitField(label="Update")

class RouteForm(FlaskForm):
    start = StringField(label=" ")
    end = StringField(label=" ")
    distance = FloatField(label=" ", validators=[DataRequired()])
    price = FloatField(label=" ", validators=[DataRequired()])
    email = FloatField(label="")
    calculate = SubmitField(label="Calculate")
    send = SubmitField(label="Send")
