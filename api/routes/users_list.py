from flask import Blueprint, request, jsonify
from requests import get
from jwt_func import validate_token
from helpful_scripts import encript, serializable_task
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


# Needs json with "username": "xxxx", "password": "xxxx"
@routes_user.route("/login", methods=["GET"])
def login_user():
    data = request.get_json()
    if request.method == "GET":
        try:
            username = data["username"]
            password = encript(data["password"])
            user = user_.query.filter_by(username=username).one()

            if user.password == password:
                return jsonify(
                    {
                        "message": "True",
                        "user_id": user.id,
                        "username": user.username,
                    }
                )
            return jsonify({"message": "False"})
        except Exception as e:
            return jsonify({"message": "False"})


@routes_user.route("/task_list", methods=["GET"])
def get_tasks():
    try:
        data = request.get_json()

        try:
            user = user_.query.get_or_404(data["user_id"])
        except Exception:
            return jsonify({"message": "No user found"})

        if len(user.task_list) <= 0:
            return jsonify({"message": "No task listed"})

        tasks = [serializable_task(x) for x in user.task_list]
        return jsonify({"task_list": tasks})

    except Exception:
        return jsonify({"message": "False"})
    # return jsonify(user.task_list)
