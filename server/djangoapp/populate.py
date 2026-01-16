from .models import CarMake, CarModel
from decimal import Decimal

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'], 
            description=data['description']
        ))

    car_model_data = [
        #NISSAN
        {"name":"Pathfinder", "type":"SUV", "year":2023, "car_make":car_make_instances[0],
         "engine_size":3.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":5, "seats":7,
         "colour":"Black", "price":Decimal("45000.00"), "mileage":12000, "is_available":True},
        {"name":"Qashqai", "type":"SUV", "year":2023, "car_make":car_make_instances[0],
         "engine_size":1.6, "fuel_type":"DIESEL", "gearbox":"MANUAL", "doors":5, "seats":5,
         "colour":"White", "price":Decimal("30000.00"), "mileage":8000, "is_available":True},
        {"name":"XTRAIL", "type":"SUV", "year":2023, "car_make":car_make_instances[0],
         "engine_size":2.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":5, "seats":7,
         "colour":"Silver", "price":Decimal("42000.00"), "mileage":15000, "is_available":True},

        #Mercedes
        {"name":"A-Class", "type":"HATCHBACK", "year":2023, "car_make":car_make_instances[1],
         "engine_size":1.3, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":5, "seats":5,
         "colour":"Blue", "price":Decimal("35000.00"), "mileage":5000, "is_available":True},
        {"name":"C-Class", "type":"SALON", "year":2023, "car_make":car_make_instances[1],
         "engine_size":2.0, "fuel_type":"DIESEL", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"Black", "price":Decimal("45000.00"), "mileage":10000, "is_available":True},
        {"name":"E-Class", "type":"SALON", "year":2023, "car_make":car_make_instances[1],
         "engine_size":3.0, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"White", "price":Decimal("55000.00"), "mileage":7000, "is_available":True},

        #Audi
        {"name":"A4", "type":"SALON", "year":2023, "car_make":car_make_instances[2],
         "engine_size":2.0, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"Grey", "price":Decimal("40000.00"), "mileage":8000, "is_available":True},
        {"name":"A5", "type":"COUPE", "year":2023, "car_make":car_make_instances[2],
         "engine_size":2.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":2, "seats":4,
         "colour":"Red", "price":Decimal("45000.00"), "mileage":6000, "is_available":True},
        {"name":"A6", "type":"SALON", "year":2023, "car_make":car_make_instances[2],
         "engine_size":3.0, "fuel_type":"DIESEL", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"Black", "price":Decimal("55000.00"), "mileage":9000, "is_available":True},

        #Kia
        {"name":"Sorrento", "type":"SUV", "year":2023, "car_make":car_make_instances[3],
         "engine_size":2.2, "fuel_type":"DIESEL", "gearbox":"AUTOMATIC", "doors":5, "seats":7,
         "colour":"White", "price":Decimal("42000.00"), "mileage":13000, "is_available":True},
        {"name":"Carnival", "type":"MPV", "year":2023, "car_make":car_make_instances[3],
         "engine_size":3.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":5, "seats":8,
         "colour":"Silver", "price":Decimal("48000.00"), "mileage":10000, "is_available":True},
        {"name":"Cerato", "type":"SALON", "year":2023, "car_make":car_make_instances[3],
         "engine_size":2.0, "fuel_type":"PETROL", "gearbox":"MANUAL", "doors":4, "seats":5,
         "colour":"Blue", "price":Decimal("28000.00"), "mileage":5000, "is_available":True},

        #Toyota
        {"name":"Corolla", "type":"SALON", "year":2023, "car_make":car_make_instances[4],
         "engine_size":1.8, "fuel_type":"HYBRID", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"White", "price":Decimal("30000.00"), "mileage":4000, "is_available":True},
        {"name":"Camry", "type":"SALON", "year":2023, "car_make":car_make_instances[4],
         "engine_size":2.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":4, "seats":5,
         "colour":"Black", "price":Decimal("35000.00"), "mileage":6000, "is_available":True},
        {"name":"Kluger", "type":"SUV", "year":2023, "car_make":car_make_instances[4],
         "engine_size":3.5, "fuel_type":"PETROL", "gearbox":"AUTOMATIC", "doors":5, "seats":7,
         "colour":"Silver", "price":Decimal("45000.00"), "mileage":12000, "is_available":True},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            engine_size=data.get('engine_size'),
            fuel_type=data.get('fuel_type'),
            gearbox=data.get('gearbox'),
            doors=data.get('doors'),
            seats=data.get('seats'),
            colour=data.get('colour'),
            price=data.get('price'),
            mileage=data.get('mileage'),
            is_available=data.get('is_available', True)
        )

    print("All CarMake and CarModel data populated successfully!")
clear