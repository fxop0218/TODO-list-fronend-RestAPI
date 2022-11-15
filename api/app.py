from flask import Flask, jsonify
from dotenv import load_dotenv
from routes.auth import routes_auth

app = Flask(__name__)
app.register_blueprint(routes_auth, url_prefix="/api")

@app.route("/")
def home(): 
    return jsonify({"message": "pong!"})
    
if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=5000, host="0.0.0.0")