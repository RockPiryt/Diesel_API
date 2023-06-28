#travel forms.py

# ----------------------------Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Car


#---------------------------Route Form with Queryfield
def car_choices():
    return Car.query.all()

class RouteForm(FlaskForm):
    start = StringField(label=" ")
    end = StringField(label=" ")
    distance = FloatField(label=" ", validators=[DataRequired()])
    price = FloatField(label=" ", validators=[DataRequired()])
    car = SelectField(label="Choose car from database", choices=[
        ("10.3", "Chevrolet Cruze"),
        ("10.6", "BMW 328d"),
        ("10.9", "Jaguar XF"),
        ("10.9", "Chevrolet Cruze Hatchback"),
        ("11.2", "BMW 328d xDrive Sports Wagon"),
        ("11.2", "Jaguar XE AWD"),
        ("11.9", "GMC Terrain FWD"),
        ("11.9", "GMC Terrain AWD"),
        ("13.2", "Mazda CX-5 2WD"),
        ("13.6", "Mazda CX-5 4WD"),
        ])
    car_data = QuerySelectField(label="Choose car from database", query_factory=car_choices)
    calculate = SubmitField(label="Calculate")

# --------------------------Send form to send_email method
class SendForm(FlaskForm):
    email = StringField(label="")
    send = SubmitField(label="Send email")


