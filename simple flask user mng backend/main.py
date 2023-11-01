from flask import Flask, request, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
usr = "drTrelloUser" # TODO: this to os env variable
passwd= "wOY2tdXdAgOxgBpU" # TODO: this to os env variable

client = MongoClient("mongodb://%s:%s@mongodb.net/trelloapp?ssl=true&authSource=admin" % (usr, passwd))  # MongoDB connection

# userame = drTrelloUser
# passwd = wOY2tdXdAgOxgBpU

# Database and Collection
db = client["user_auth_db"]
users_collection = db["users"]

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Both username and password are required"}), 400

    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(password, method="sha256")

    new_user = {"username": username, "password": hashed_password}
    users_collection.insert_one(new_user)

    return jsonify({"message": "Registration successful"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Both username and password are required"}), 400

    user = users_collection.find_one({"username": username})

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
