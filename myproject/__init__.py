#__init__.py 
#Create app and db

# -----------------------------------Imports
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# -----------------------------------Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0s112'
bootstrap = Bootstrap5(app)

# -----------------------------------Create DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# Migrate(app,db)


# -----------------------------------Register Blueprints
from myproject.single_page.views import single_page_blueprint
from myproject.top_cars.views import edit_car_blueprint
from myproject.travel.views import travel_blueprint

app.register_blueprint(single_page_blueprint, url_prefix='/single-page')
app.register_blueprint(edit_car_blueprint, url_prefix='/edit-car')
app.register_blueprint(travel_blueprint, url_prefix='/travel')

#--------------------------------Create views
@app.route("/", methods=["GET", "POST"])
def start():
    '''Main page'''
    return render_template("start.html")




