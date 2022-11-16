from flask import Blueprint, request, jsonify
from jwt_func import validate_token
from datetime import datetime, timedelta
from models import task, user_
from database import db

routes_task = Blueprint("routes_task", __name__)

# Token verification


@routes_task.before_request
def verify_token_middleware():
    token = request.headers["Authorization"].split(" ")[1]
    validate_token(
        token, False
    )  # Only returns values if hava a error if return ANY value dosen't continue


# Need json file with "title", "text" and start_data, and finish_data (optional)
@routes_task.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    if request.method == "POST":
        try:
            title = data["product"]["title"]
            text = data["product"]["text"]
            try:
                created = data["product"]["start_data"]
            except Exception:
                created = datetime.now()
            try:
                closed = data["product"]["finish_data"]
            except Exception:
                closed = datetime.now() + timedelta(2)
            new_task = task(title=title, text=text, created=created, closed=closed)
            db.session.add(new_task)

            try:
                task_user = user_.query.get_or_404(data["user"]["user_id"])
                task_user.task_list.append(new_task)
                db.session.commit()
                return jsonify({"message": "True"})
            except Exception:
                return jsonify({"message": "False"})
            return jsonify({"message": "True"})
        except Exception:
            return jsonify({"message": "False"})

    return jsonify({"message": "False"})
