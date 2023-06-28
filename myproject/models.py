# models.py
#Create db.model


# --------------------Import db instance from __init__.py file
from myproject import db



# --------------------Create db.Model
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
        return f'{self.make} [{self.model}] {self.consumption} L'
