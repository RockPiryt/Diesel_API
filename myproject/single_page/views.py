#view single-page

# -----------------------------------Imports
from flask import Blueprint, render_template, redirect, url_for, request

from myproject import db
from myproject.models import Car
from myproject.forms import RouteForm

from myproject.trading.stock_trading import Article, title_articles, description_articles, url_articles, COMPANY_NAME, arrow, diff_percent

import requests

#--------------------------------Create Blueprint
single_page_blueprint = Blueprint('single-page', __name__, template_folder='templates/single_page')

# # --------------------------------Create table Car from models.py
# db.create_all()

# --------------------------------Add values to database
# dataset_id="all-vehicles-model"
OPENDATA_VEHICLE_URL = f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=all-vehicles-model&q=&rows=200&sort=-barrels08&facet=make&facet=model&facet=cylinders&facet=drive&facet=eng_dscr&facet=fueltype&facet=fueltype1&facet=mpgdata&facet=phevblended&facet=trany&facet=vclass&facet=year&refine.fueltype=Diesel&exclude.year=1984&exclude.year=1985"

# Make API request - 60 rows - 
# iteration by 2 (to eliminate duplicate model with different transmission)
# response = requests.get(OPENDATA_VEHICLE_URL)
# all_cars = response.json()["records"][::2]

# # Get specific information
# for one_car in all_cars:
#     new_car = Car(
#         make=one_car["fields"]["make"],
#         model=one_car["fields"]["model"],
#         year=one_car["fields"]["year"],
#         engine=one_car["fields"]["displ"],
#         fuel=one_car["fields"]["fueltype1"],
#         transmission=one_car["fields"]["trany"],
#         size=one_car["fields"]["vclass"],
#         consumption=one_car["fields"]["barrels08"],
#     )
#     #Add information to database
#     db.session.add(new_car)
#     db.session.commit()

#--------------------------------Create views
@single_page_blueprint.route("/", methods=["GET", "POST"])
def home():
    '''Main page'''

    ####################Stock trading information Section############################
    # Stock trading information
    first_article = Article(
        title=title_articles[0],
        description=description_articles[0],
        url=url_articles[0]
        )
    
    second_article = Article(
        title=title_articles[1],
        description=description_articles[1],
        url=url_articles[1]
        )
    
    third_article = Article(
        title=title_articles[2],
        description=description_articles[2],
        url=url_articles[2]
        )
    ####################Top Car CRUD database Section###############################
    # Show 10 cars in database
    num_page=request.args.get('num_page', 1, type=int)
    all_cars_pagination = Car.query.paginate(page=num_page, per_page=10)
    
    ####################Travel Calculator Section###############################
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

        return redirect(url_for('travel.travel_info',
                                travel_user_start=user_start,
                                travel_user_end=user_end,
                                travel_user_distance=user_distance,
                                travel_consumption=user_car_consumption,
                                travel_diesel_consumption=diesel_consumption,
                                travel_cost=user_cost,
                                ))

    return render_template("index.html", 
                           html_all_cars_pagination=all_cars_pagination,
                           html_form=route_form, 
                           html_first_article=first_article,html_second_article=second_article,
                           html_third_article=third_article,
                           html_company_name=COMPANY_NAME,
                           html_arrow=arrow,
                           html_diff_percent=diff_percent,
                           )

