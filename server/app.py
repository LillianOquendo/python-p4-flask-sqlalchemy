from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#after exporting and running flask db init we have the following warning in the terminal without the below line
#(Please edit configuration/connection/logging settings in '/python-p4-flask-sqlalchemy/server/migrations/alembic.ini' before proceeding.)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#with the above line included in our app.py we can go straight into migration with flask db revision --autogenerate -m'Create tables owners, pets
#we then push those migrations into our database with flask db upgrade head
migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)