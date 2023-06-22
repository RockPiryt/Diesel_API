from flask import Flask, render_template, redirect, url_for
from models import db, Car
import requests
from flask import request
from flask_bootstrap import Bootstrap5
from forms import EditForm, RouteForm, SendForm
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage


# Get user info to send email
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
my_email = os.getenv("MY_EMAIL")
api_key_gmail = os.getenv("APP_PASSWORD_GMAIL")

# dataset_id="all-vehicles-model"
OPENDATA_VEHICLE_URL = f"https://public.opendatasoft.com//api/records/1.0/search/?dataset=all-vehicles-model&q=&rows=20&sort=-barrels08&facet=make&facet=model&facet=cylinders&facet=drive&facet=eng_dscr&facet=fueltype&facet=fueltype1&facet=mpgdata&facet=phevblended&facet=trany&facet=vclass&facet=year&refine.fueltype1=Diesel&refine.year=2018"


# -----------------------------------Create app
app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0s112'
app.secret_key = "MyPassword12345"
bootstrap = Bootstrap5(app)

# -----------------------------------Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()


db.create_all()
# --------------------------------Add values to database
# Make API request - 20 rows - iteration by 2 (to eliminate duplicate model with different transmission)
response = requests.get(OPENDATA_VEHICLE_URL)
all_cars = response.json()["records"][::2]

# Get specific information
for one_car in all_cars:
    new_car = Car(
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


# -----------------------------------URLS

@app.route("/", methods=["GET", "POST"])
def home():
    '''Main page'''

    # Show all cars in database
    python_all_cars = Car.query.all()
    # Slice to show 10 cars
    list_all_cars = python_all_cars[0:10]
    # Create route form
    route_form = RouteForm()

    # Get information from form
    if route_form.validate_on_submit():
        user_start = route_form.start.data
        user_end = route_form.end.data
        user_distance = route_form.distance.data
        diesel_price = route_form.price.data
        user_car_consumption = float(route_form.car.data)
        # Calculate travel cost
        diesel_consumption = user_distance/100 * user_car_consumption
        user_cost = diesel_consumption * diesel_price

        return redirect(url_for('travel_info',
                                travel_user_start=user_start,
                                travel_user_end=user_end,
                                travel_user_distance=user_distance,
                                travel_consumption=user_car_consumption,
                                travel_diesel_consumption=diesel_consumption,
                                travel_cost=user_cost,
                                ))

    return render_template("index.html", html_all_cars=list_all_cars, html_form=route_form)


def send_email(distance, cost):
    # Create email
    user_info = f"""
    Here are information from user: \n
    Distance: {distance}, \n
    Travel cost: {cost}, \n
    """
    msg = EmailMessage()
    msg.set_content(user_info)
    msg["Subject"] = "Travel cost"
    msg["From"] = my_email
    msg["To"] = my_email

    # Send email with form's information
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=api_key_gmail)
        connection.send_message(msg)


@app.route("/travel", methods=["GET", "POST"])
def travel_info():
    '''Show travel information and a form to send email.'''

    new_start = request.args.get("travel_user_start")
    new_end = request.args.get("travel_user_end")
    new_distance = float(request.args.get("travel_user_distance"))
    new_consumption = float(request.args.get("travel_consumption"))
    new_diesel_consumption = float(
        request.args.get("travel_diesel_consumption"))
    new_cost = float(request.args.get("travel_cost"))

    send_form = SendForm()

    return render_template("travel_info.html",
                           html_send_form=send_form,
                           html_new_start=new_start,
                           html_new_end=new_end,
                           html_new_distance=new_distance,
                           html_new_consumption=new_consumption,
                           html_new_diesel_consumption=new_diesel_consumption,
                           html_new_cost=new_cost, )


@app.route("/edit", methods=["GET", "POST"])
def add_img():
    '''Add image source'''

    # Get car from db to edit
    id_car_to_edit = request.args.get("car_id")
    car_to_edit = Car.query.get(id_car_to_edit)

    # Create flaskform to edit car image
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        car_to_edit.img_url = edit_form.img_source.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_car.html", html_form=edit_form, html_car_to_edit=car_to_edit)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000", use_reloader=False)
