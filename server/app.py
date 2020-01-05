import os
from flask import Flask, session, current_app
from db_instance import db
import psycopg2
from smsAPI import sms_api
from socialAPI import social_api
from statusAPI import status_api
from emailAPI import email_api
from usersAPI import users_api

# creats the correct path for the db file
project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

# creates app, registers blueprint, and 
# returns the app for use in the main.py file
def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=os.environ["DB_USER"],pw=os.environ["DB_PASS"],url=os.environ["DB_URL"],db=os.environ["DB_NAME"])
    app.config['SQLALCHEMY_ECHO'] = True
    app.register_blueprint(sms_api)
    app.register_blueprint(social_api)
    app.register_blueprint(status_api)
    app.register_blueprint(email_api)
    app.register_blueprint(users_api)
    app.secret_key = os.environ["SECRET_KEY"]
    db.init_app(app)
    return app


# this actually keeps db refreshed if new tables are added
def setup_database(app):
    with app.app_context():
        db.create_all()