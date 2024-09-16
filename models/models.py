from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    activities = db.relationship('Activity', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # duração em minutos
    calories_burned = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Float, nullable=True)  # nova métrica, em quilômetros
    exercise_type = db.Column(db.String(50), nullable=True)  # nova métrica, tipo de exercício
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Activity {self.name} - {self.duration} min>'
