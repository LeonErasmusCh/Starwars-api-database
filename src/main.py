"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favourites, People, Planets, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    return jsonify(all_users), 200


#ruta que mostrara todos mis FAVOURITES
@app.route('/favourites', methods=['GET'])
def allFavourites():
    all_favoutites = Favourites.query.all()
    all_favoutites = list(map(lambda x: x.serialize(), all_favourites))
    return jsonify(all_favourites)    

@app.route('/user/favourites', methods=['GET'])
def allUserFavourites():
    all_user_favoutites = Favourites.query.all()
    all_user_favoutites = list(map(lambda x: x.serialize(), all_user_favoutites))
    return jsonify(all_user_favoutites)    

@app.route('/user/favourites<int:position>', methods=['POST'])
def PostFavourites():
    all_user_favoutites = Favourites.query.all()
    all_user_favoutites = list(map(lambda x: x.serialize(), all_user_favoutites))
    return jsonify(all_user_favoutites)    

@app.route('/user/favourites<int:position>', methods=['DELETE'])
def DeleteFavourites():
    delete_user_favoutites = Favourites.query.all()
    delete_user_favoutites = list(map(lambda x: x.serialize(), delete_user_favoutites))
    return jsonify(delete_user_favoutites)    


#ruta que mostrara todos mis PEOPLE
@app.route('/people', methods=['GET'])
def allPeople():
    all_people = People.query.all()
    all_people = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_people)   


#ruta que mostrara todos mis PLANTES
@app.route('/planets', methods=['GET'])
def allPlanets():
    all_planets = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planets))
    return jsonify(all_planets)   



#ruta que mostrara todos mis VEHICLES
@app.route('/vehicles', methods=['GET'])
def allVehicles():
    all_vehicles = Vehicles.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), all_vehicles))
    return jsonify(all_vehicles) 









# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
