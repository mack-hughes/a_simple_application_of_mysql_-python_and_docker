from src import UserRepo
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world"

@app.route("/insert", methods=["GET"])
def insert():
    return "Ola, esou na aplicação setaada"

    userRepo = UserRepo()
    body = request.json 

    userRepo.insert_user(body["name"])

    return "ok"