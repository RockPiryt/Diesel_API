#top_car views.py

#--------------------------------Imports
from flask import Blueprint, render_template, redirect, url_for, request,flash
from myproject import db
from myproject.models import Car
from myproject.top_cars.forms import AddCarForm,EditForm

#--------------------------------Create Blueprint
edit_car_blueprint = Blueprint('edit-car', __name__, template_folder='templates/top_cars')


#--------------------------------Create views

@edit_car_blueprint.route("/add-new-car", methods=["GET", "POST"])
def add_new_car():
    '''Add new car to database'''

    # # Create flaskform to add new car
    add_form = AddCarForm()
    if add_form.validate_on_submit():
        new_car = Car(
            make=add_form.make.data,
            model=add_form.model.data,
            year=add_form.year.data,
            engine=add_form.engine.data,
            fuel=add_form.fuel.data,
            transmission=add_form.transmission.data,
            size=add_form.size.data,
            consumption=add_form.consumption.data,
            img_url=add_form.img_source.data,
        )
        #Add information to database
        db.session.add(new_car)
        db.session.commit()

        return redirect(url_for('single-page.home'))
    return render_template("add_new_car.html", html_form=add_form)



@edit_car_blueprint.route("/edit-car", methods=["GET", "POST"])
def edit_img_car():
    '''Edit image source'''

    # Get car from db to edit
    id_car_to_edit = request.args.get("car_id")
    car_to_edit = Car.query.get(id_car_to_edit)

    # Create flaskform to edit car image
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        car_to_edit.img_url = edit_form.img_source.data
        db.session.commit()
        return redirect(url_for('single-page.home'))
    return render_template("edit_car.html", html_form=edit_form, html_car_to_edit=car_to_edit)


@edit_car_blueprint.route("/delete-car", methods=["GET", "POST"])
def delete_car():
    '''Delete car from database'''

    # Get car from db to edit
    id_car_to_del = request.args.get("car_id")
    car_to_del = Car.query.get(id_car_to_del)
    db.session.delete(car_to_del)
    db.session.commit()
    flash(f'{car_to_del.make} {car_to_del.model} {car_to_del.year} Successfully deleted', 'success')

    return redirect(url_for('single-page.home'))
