from flask import Flask, jsonify
from dotenv import load_dotenv
from models import user_, task
from routes.auth import routes_auth # Use venv interprete ()
from routes.task_list import routes_task
from routes.users_list import routes_user
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "task_list_db"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/user")
app.register_blueprint(routes_task, url_prefix="/task")


@app.route("/")
def home():
    return jsonify({"message": "test"})


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=5000, host="0.0.0.0")
