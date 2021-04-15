from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import User, Car, car_schema, cars_schema, db, ma

api = Blueprint('api',__name__,url_prefix='/api') #the url that goes into insomnia

@api.route('/getdata')
def getdata():
    return {'some':'value'}

# CREATE CAR ENDPOINT
@api.route('/cars', methods = ['POST']) #where is /cars referenced?
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    condition = request.json['condition']
    cost = request.json['cost']
    user_token = current_user_token.token

    car=Car(make,model,year,condition,cost,user_token = user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response) #what are we doing here again

# RETRIEVE ALL CARS ENDPOINT
@api.route('/cars', methods = ['GET'])
@token_required #this is to make sure that user is signed in right?
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all() #get all of them
    response = cars_schema.dump(cars)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id): #id from @ is coming here at id
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)

# UPDATE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)

    car.make = request.json['make']
    car.model = request.json['model']
    car.year = request.json['year']
    car.condition = request.json['condition']
    car.cost = request.json['cost']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# DELETE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token,id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)