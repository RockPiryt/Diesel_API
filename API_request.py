import requests

dataset_id="all-vehicles-model"
OPENDATA_VEHICLE_URL = f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=all-vehicles-model&q=&sort=year&facet=make&facet=model&facet=fueltype&facet=trany&facet=vclass&facet=year&refine.make=Volkswagen&refine.model=Golf"


response = requests.get(OPENDATA_VEHICLE_URL)
# print(response.text) - all from response
cars = response.json()

####################TEST
# nhits_status= response.json()["nhits"]
# print(nhits_status) 76

# records_status= response.json()["records"]
# print(records_status)

# records= response.json()["records"][0]
# print(records)

records_fields= response.json()["records"][0]["fields"]["trany"]
#first value transmission information
# print(records_fields) #object[0].trany = Manual 6-spd

all_car = response.json()["records"] #list with all records (10 rows)
# print(all_car)

#Get specific information
for one_car in all_car:
    car_trany = one_car["fields"]["trany"]
    print(car_trany)
    car_year = one_car["fields"]["year"]
    print(car_year)


