from flask import Blueprint, request, jsonify
from requests import get
from jwt_func import validate_token
from helpful_scripts import encript
from models import user_
from database import db

routes_user = Blueprint("routes_user", __name__)

# Token verification


@routes_user.before_request
def verify_token_middleware():
    token = request.headers["Authorization"].split(" ")[1]
    validate_token(
        token, False
    )  # Only returns values if hava a error if return ANY value dosen't continue


@routes_user.route("/list", methods=["GET"])
def user_list():
    return jsonify({"exemple": "exemple"})


@routes_user.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    if request.method == "POST":
        try:
            user = data["username"]
            password = encript(data["password"])
            new_user = user_(username=user, password=password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "True"})

        except Exception as e:
            return jsonify({"message": "False"})


@routes_user.route("/login", methods=["GET"])
def login_user():
    data = request.get_json()
    if request.method == "GET":
        try:
            username = data["username"]
            password = encript(data["password"])
            user = user_.query.filter_by(username=username).one()

            if user.password == password:
                return jsonify({"message": "True"})
            return jsonify({"message": "False"})
        except Exception as e:
            return jsonify({"message": "False"})
