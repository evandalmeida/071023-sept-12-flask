from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates 
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Park(db.Model):
    __tablename__ = 'parks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    size = db.Column(db.Integer)

    animals = db.relationship('Animal', back_populates='park')


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))

    park = db.relationship('Park', back_populate='animals')

import ipdb; ipdb.set_trace()