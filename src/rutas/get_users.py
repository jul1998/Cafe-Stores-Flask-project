import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import User
from flask import Flask, url_for
from datetime import datetime
import json
from ..utils import APIException

@app.route("/get_users", methods=["POST"])
def users():
    user_id = request.get_json()
    
    user_query = User.query.filter_by(id=user_id).first()
    print(user_query.email)
    return jsonify({"email":user_query.email})