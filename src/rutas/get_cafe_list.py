import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Cafe
from flask import Flask, url_for
from datetime import datetime
import json
from ..utils import APIException

@app.route("/cafe_list", methods=["GET","POST"])
def get_cafes():
    if request.method == 'POST':
        body = request.get_json()
        try:
            name = body["name"]
            map_url = body["map_url"]
            img_url = body["img_url"]
            location = body["location"]
            coffee_price = body["coffee_price"]
            favorite_cafe = body["user"]

            new_cafe_store = Cafe(name=name,
            map_url=map_url, 
            img_url=img_url,
            location=location,
            coffee_price=coffee_price)
            favorite_cafe=favorite_cafe


        except Exception:
            db.session.rollback()
            return jsonify({"msg":"Cafe store was not added for some error"})
        else:

            db.session.add(new_cafe_store)
            db.session.commit()
            return jsonify({"msg":"Cafe store added"})
    else: #Get request

        all_cafe_stores_query = Cafe.query.all()
        cafe_list = [cafe.serialize() for cafe in all_cafe_stores_query]
        print(cafe_list[0])

        return jsonify(cafe_list)
