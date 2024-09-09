from flask import Blueprint, request, jsonify
from models import db, User, Activity

# Criando um Blueprint para as rotas de usuários e atividades
main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

@main.route('/add_activity', methods=['POST'])
def add_activity():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    new_activity = Activity(name=data['name'], duration=data['duration'], calories_burned=data['calories_burned'],
                            user_id=user.id)
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({"message": "Activity added"}), 201

@main.route('/user/<username>/activities', methods=['GET'])
def get_user_activities(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    activities = Activity.query.filter_by(user_id=user.id).all()
    activities_list = [
        {"name": activity.name, "duration": activity.duration, "calories_burned": activity.calories_burned} for activity
        in activities]

    return jsonify({"user": user.username, "activities": activities_list})
