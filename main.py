from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
@app.route("/")
def home():
    '''Show all cars in database'''
    all_cars = Car.query.all()
    return render_template("index.html", html_all_cars=all_cars)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
