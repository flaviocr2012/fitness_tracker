from models import Activity
from repositories.activity_repository import ActivityRepository

class ActivityService:

    @staticmethod
    def add_activity(data, user):
        new_activity = Activity(
            name=data['name'],
            duration=data['duration'],
            calories_burned=data['calories_burned'],
            user_id=user.id
        )
        ActivityRepository.add_activity(new_activity)
        return {"message": "Activity added"}, 201

    @staticmethod
    def get_activities_by_user(user_id):
        return ActivityRepository.find_by_user_id(user_id)
