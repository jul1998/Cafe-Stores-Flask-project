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
   
   def serialize(self):
      return{
         "id":self.id,
         "name": self.name,
         "user_cafe_favorite":self.user_cafe_favorite,
         "img_url":self.img_url
      }
  
   
