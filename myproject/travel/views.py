#travel views.py

#--------------------------------Imports
from flask import Blueprint, render_template, request
from myproject.travel.forms import SendForm

import os
from os.path import join, dirname
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
#--------------------------------Create Blueprint
travel_blueprint = Blueprint('travel', __name__, template_folder='templates/travel')

#----------------------------- Get user info to send email
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
my_email = os.getenv("MY_EMAIL")
api_key_gmail = os.getenv("APP_PASSWORD_GMAIL")



#--------------------------------Create views
@travel_blueprint.route("/info", methods=["GET", "POST"])
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
