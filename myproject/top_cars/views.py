#top_car views.py

#--------------------------------Imports
from flask import Blueprint, render_template, redirect, url_for,request
from myproject import db
from myproject.models import Car
from myproject.top_cars.forms import EditForm

#--------------------------------Create Blueprint
edit_car_blueprint = Blueprint('edit-car', __name__, template_folder='templates/top_cars')


#--------------------------------Create views
@edit_car_blueprint.route("/add-img", methods=["GET", "POST"])
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