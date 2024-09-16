from flask import Flask
from models import db
from controllers import main
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)  # Inicialize o Flask-Migrate

# Registrando o Blueprint
app.register_blueprint(main)

# Crie as tabelas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
