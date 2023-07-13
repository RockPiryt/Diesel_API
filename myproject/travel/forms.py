#travel forms.py

# ----------------------------Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from myproject.models import Car


#---------------------------Route Form with Queryfield
def car_choices():
    return Car.query.all()

class RouteForm(FlaskForm):
    start = StringField(label=" ")
    end = StringField(label=" ")
    distance = FloatField(label=" ", validators=[DataRequired()])
    price = FloatField(label=" ", validators=[DataRequired()])
    car_data = QuerySelectField(label="Choose car from database", query_factory=car_choices)
    calculate = SubmitField(label="Calculate")

# --------------------------Send form to send_email method
class SendForm(FlaskForm):
    email = StringField(label="")
    send = SubmitField(label="Send email")


