import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    last_name = Column(String(30))
    username = Column(String(20), unique=True)
    email = Column(String(40), unique=True)
    password = Column(String(20))
    favorite = relationship('Favorite', back_populates='user')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    gender = Column(String(20))
    specie = Column(String(10))
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet', back_populates='characters')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))
    characters = relationship('Character', back_populates='planet')

    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(100))
    passengers = Column(Integer)
    crew = Column (Integer)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')