from ..db import db
import os

class Cafe(db.Model):
     __tablename__ = "cafe" 
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(250), unique=True, nullable=False)
     map_url = db.Column(db.String(500), nullable=True)
     img_url = db.Column(db.String(500), nullable=True)
     location = db.Column(db.String(250), nullable=True)
     coffee_price = db.Column(db.String(250), nullable=True)
     user_cafe_favorite = db.Column(db.Integer, db.ForeignKey("user.id"))

     def to_dict(self):
        return {column.name:getattr(self,column.name) for column in self.__table__.columns}