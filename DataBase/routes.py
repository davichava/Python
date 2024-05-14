from flask import Flask, jsonify, session

from DataBase.models import User
app = Flask(__name__)

@app.route("/users", methods=['GET'])
def get_users():
    users = session.query(User).all()
    return jsonify([user.name for user in users])