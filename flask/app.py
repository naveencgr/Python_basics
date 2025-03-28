from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import threading

app = Flask(__name__)
api_bp = Blueprint('api', __name__, url_prefix="/myproject")
CORS(app) 

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"message": "API is working"})

@api_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()
    name = ''
    if 'name' in data:
        name = data['name']

    print(name)    

@api_bp.route("/background_thread")
def background_thread():
    def task():
        print("task")
    thread = threading.Thread(target= task, name ="background_task_name")
    thread.start()
    # This will create a background thread to overcome the gateway timeouts

app.register_blueprint(api_bp)    