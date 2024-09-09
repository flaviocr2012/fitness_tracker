from flask import Flask

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crie as tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Fitness Tracker API"

if __name__ == '__main__':
    app.run(debug=True)
