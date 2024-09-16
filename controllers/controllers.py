from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.activity_service import ActivityService

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    response, status = UserService.add_user(data)
    return jsonify(response), status

@main.route('/add_activity', methods=['POST'])
def add_activity():
    data = request.get_json()
    user = UserService.get_user_by_username(data['username'])
    if not user:
        return jsonify({"error": "User not found"}), 404
    response, status = ActivityService.add_activity(data, user)
    return jsonify(response), status

@main.route('/user/<username>/activities', methods=['GET'])
def get_user_activities(username):
    user = UserService.get_user_by_username(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    activities = ActivityService.get_activities_by_user(user.id)
    activities_list = [
        {
            "name": activity.name,
            "duration": activity.duration,
            "calories_burned": activity.calories_burned,
            "distance": activity.distance,
            "exercise_type": activity.exercise_type,
        } for activity in activities
    ]

    return jsonify({"user": user.username, "activities": activities_list})
