from models import User
from repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def add_user(data):
        new_user = User(username=data['username'], email=data['email'])
        UserRepository.add_user(new_user)
        return {"message": "User added"}, 201

    @staticmethod
    def get_user_by_username(username):
        return UserRepository.find_by_username(username)
