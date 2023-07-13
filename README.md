# Diesel_API

This web application provides a wide range of information about diesel
and costs associated with it. User can follow current diesel price trends. Moreover user can calculate a cost of driving a diesel car. In addition, he can compare cars with the lowest fuel consumption.

## Table of Contents

* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Previews](#Previews)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
* [License](#license)

## General Information

I created this web application to show travel cost using diesel cars. Therefore I use API request to get information about changes in diesel price.

Moreover User can calculate travel cost. User fill in route form and get information about travel cost between 2 cities in Poland.

This application was created using Flask and PostgreSQL database.

## Technologies Used

- Python - version 3.11
- Bootstrap - version 5.2.3
- Flask - version 2.2.2
- SQLAlchemy - version 1.4.45
- WTForms - version  3.0.1
- PostgreSQL database

## Features

List the ready features here:

- In Stock trading section User can follow current information about diesel from stock trading (use API),
- In top cars section there are showed cars from database, (PostgreSQL database)
- User can add new car, edit image car in database or delete car from database,
- In Travel cost section User can add information about travel in route form, choose car from database and make calculation to get information about cost. 

## Previews

### Home Page
![Home Page Preview](myproject/static/img/previews/prev_home_page.jpg)

### Section 1 - Stock trading information using API
![Section 1 Preview - Stock trading information using API](myproject/static/img/previews/prev_section_1_stock_trading.jpg)

### Section 2 - Gas station
![Section 2 Preview - Gas station](myproject/static/img/previews/prev_section_2_gas_station.jpg)

### Section 3 - Car database with CRUD operations
![Section 3 Preview - Car database with CRUD operations](myproject/static/img/previews/prev_section_3_cars_db.jpg)

### Section 4 - Travel cost calculator with cars from database
![Section 4 Preview - Travel cost calculator with cars from database](myproject/static/img/previews/prev_section_4_travel_cost_calculator.jpg)

## Setup

- Clone This Project git clone
- Enter Project Directory cd Disiel_API
- Create a Virtual Environment (for Windows) py -m venv (name your virtual enviroment :) venv

'EXAMPLE: py -m venv venv'

- Activate Virtual Environment source: venv/Scripts/activate
- Install Requirements Package pip install -r requirements.txt
- Finally Run The Project: python app.py

## Project Status

Project is: _in progress_

## Room for Improvement

Room for improvement:

- Login and registering user with authentication,
- Registered users can calculate and save travel cost in database,
- Webscraping Google Maps to get distance between 2 cities in Poland - this distance will be used in route form.
- Prepare application to deploy on AWS.

To do:

- add login/register routes
- create model to keep information about travel
- use Selenium to get distance beetween 2 cities in Poland
- change structure to deploy structure

## Contact

- Created by [@RockPiryt Github](https://github.com/RockPiryt)
- My Resume [@RockPiryt Resume](https://rockpiryt.github.io/Personal_Site/)

Feel free to contact me!

## License

This project is open source and available under the [MIT License]
