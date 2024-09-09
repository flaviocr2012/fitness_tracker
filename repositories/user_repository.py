from models import User, db

class UserRepository:

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
