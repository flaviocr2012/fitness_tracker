from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    crated_at = db.Column(db.DateTime, default=datetime.utcnow)

    activites = db.relationship('Activity', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
