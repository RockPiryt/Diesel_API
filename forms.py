from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
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
    car = SelectField(label="Choose car from database", choices=[
        ("Chevrolet_[Cruze]", "Chevrolet Cruze"),
        ("BMW_[328d]", "BMW 328d"),
        ("Jaguar_[XF]", "Jaguar XF"),
        ("Chevrolet_[Cruze Hatchback]", "Chevrolet Cruze Hatchback"),
        ("BMW_[328d xDrive Sports Wagon]", "BMW 328d xDrive Sports Wagon"),
        ("Jaguar_[XE AWD]", "Jaguar XE AWD"),
        ("GMC_[Terrain FWD]", "GMC Terrain FWD"),
        ("GMC_[Terrain AWD]", "GMC Terrain AWD"),
        ("Mazda_[CX-5 2WD]", "Mazda CX-5 2WD"),
        ("Mazda_[CX-5 4WD]", "Mazda CX-5 4WD"),
        ])
    email = StringField(label="")
    calculate = SubmitField(label="Calculate")
