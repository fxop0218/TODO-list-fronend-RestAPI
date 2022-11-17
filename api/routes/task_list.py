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
        except Exception:
            return jsonify({"message": "False"})

    return jsonify({"message": "False"})


@routes_task.route("/add", methods=["POST"])
def add_uses():
    data = request.get_json()
    if request.method == "POST":
        try:
            task_id = data["task_id"]
            user_id = data["user_id"]
            new_user_id = data["new_users_id"]  # array

            try:
                task_ = task.query.get_or_404(task_id)
            except Exception:
                return jsonify({"message": "Task does not exist"})

            if len(new_user_id) <= 0:
                return jsonify({"message": "No task added"})
            admin_user = user_.query.get_or_404(user_id)
            print(f"Admin task list: {admin_user.task_list}")
            if task_ not in (admin_user.task_list):
                return jsonify({"message": "User without this task"})

            for user in new_user_id:
                new_user = user_.query.get(user)
                if task_id not in new_user.task_list:
                    new_user.task_list.append(task_)
            db.session.commit()
            return jsonify({"message": "True"})

        except Exception as e:
            return jsonify({"message": "False"})


@routes_task.route("/delete", methods=["POST"])
def delete_task():
    try:
        if request.method == "POST":
            data = request.get_json()
            user_id = data["user_id"]
            task_id = data["task_id"]

            try:
                user = user_.query.get_or_404(user_id)
                task_ = task.query.get_or_404(task_id)
            except Exception:
                return jsonify({"message": "Task or user erro"})

            if task_ not in user.task_list:
                return jsonify({"message": "This task dosn't exists in your list"})

            try:
                db.session.delete(task_)
                db.session.commit()
            except Exception:
                return jsonify({"message": "Error deleting task"})
        return jsonify({"message": "True"})
    except Exception: return jsonify({"message": "False"})


@routes_task.route("/test", methods=["GET", "POST"])
def test():
    data = request.get_json()
    if request.method == "POST":
        exemple = data["exemple"]
        n_exemple = len(exemple)
        return jsonify({"message": n_exemple})
