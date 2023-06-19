from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests


dataset_id="all-vehicles-model"
OPENDATA_VEHICLE_URL = f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=all-vehicles-model&q=&sort=year&facet=make&facet=model&facet=fueltype&facet=trany&facet=vclass&facet=year&refine.make=Volkswagen&refine.model=Golf"

##-----------------------------------Create app
app = Flask(__name__)

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
# )

# db.session.add(new_car)
# db.session.commit()


##-----------------------------------URLS
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

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
