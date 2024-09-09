from models import Activity, db

class ActivityRepository:

    @staticmethod
    def add_activity(activity):
        db.session.add(activity)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id):
        return Activity.query.filter_by(user_id=user_id).all()
