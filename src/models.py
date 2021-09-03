from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavourite = db.Column(db.String(30), unique= False, nullable=False)
    typeFavourite = db.Column(db.String(30), unique= False, nullable=False)
    rel = db.relationship('User')
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nameFavourite": self.nameFavourite,
            "typeFavourite": self.typeFavourite
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True, nullable=False)
    homeworld = db.Column(db.String(30), unique= False, nullable=False)
    age = db.Column(db.Integer)
    vehicle = db.Column(db.String(30), unique= False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            "vehicle": self.vehicle,
            "age": self.age,
            # do not serialize the password, its a security breach
        }



class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True, nullable=False)
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population
        }



class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True, nullable=False)
    crew = db.Column(db.Integer)
    load_capacity = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "load_capacity": self.load_capacity
        }        

