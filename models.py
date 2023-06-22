from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


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
    

# # -----------------------------First information to db to check db
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