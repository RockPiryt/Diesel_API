from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import request
from flask_bootstrap import Bootstrap5



#dataset_id="all-vehicles-model"
OPENDATA_VEHICLE_URL = f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=all-vehicles-model&q=&sort=year&facet=make&facet=model&facet=fueltype&facet=trany&facet=vclass&facet=year&refine.make=Volkswagen&refine.model=Golf"

##-----------------------------------Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0s112'
bootstrap = Bootstrap5(app)

##-----------------------------------Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.app_context().push()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    engine = db.Column(db.Float, nullable=True)
    fuel = db.Column(db.String, nullable=False)
    transmission = db.Column(db.String, nullable=True)
    size = db.Column(db.String, nullable=True)
    consumption = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String, nullable=True)


    def __repr__(self):
        return f'<Vehicle {self.model}>'

db.create_all()

# # First information to db
# new_car = Car(
#     make = "Volkswagen",
#     model = "Golf",
#     year = 2019,
#     engine = 1.4,
#     transmission = "Manual 6-spd",
#     fuel = "Regular",
#     size = "Compact Cars",
#     consumption = 10.300,
#     img_url="https://images.unsplash.com/photo-1614152204322-e6ab7f040c1d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
# )

# db.session.add(new_car)
# db.session.commit()

##------------------------------Flaskforms
class EditForm(FlaskForm):
    img_source = StringField(label="Please paste url to car image", validators=[DataRequired()])
    submit = SubmitField(label="Update")



#-----------------------------------URLS
# @app.route("/")
# def home():
#     '''Show all cars in database'''
#     all_cars = Car.query.all()
#     return render_template("index.html", html_all_cars=all_cars)

@app.route("/")
def home():
    '''Show all cars in database'''

    #Make API request - 10 rows
    response = requests.get(OPENDATA_VEHICLE_URL)
    all_cars = response.json()["records"]

    #Get specific information
    for one_car in all_cars:
        new_car=Car(
            make=one_car["fields"]["make"],
            model=one_car["fields"]["model"],
            year=one_car["fields"]["year"],
            engine=one_car["fields"]["displ"],
            fuel=one_car["fields"]["fueltype1"],
            transmission=one_car["fields"]["trany"],
            size=one_car["fields"]["vclass"],
            consumption=one_car["fields"]["barrels08"],
        )
        db.session.add(new_car)
        db.session.commit()

    python_all_cars = Car.query.all()
    return render_template("index.html", html_all_cars=python_all_cars)

@app.route("/add-img", methods=["GET", "POST"])
def add_img():
    '''Add image source'''

    #Get car from db to edit
    id_car_to_edit = request.args.get("car_id")
    car_to_edit = Car.query.get(id_car_to_edit)

    #Create flaskform to edit car image
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        car_to_edit.img_url = edit_form.img_source.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_car.html", html_form=edit_form, html_car_to_edit=car_to_edit)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
