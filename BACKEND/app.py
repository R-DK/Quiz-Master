from flask import Flask
from application.database import db
from application.models import User, Role
from application.config import LocalDevelopmentConfig
from flask_security import Security, SQLAlchemyUserDatastore


# Function to create the Flask Application
def create_app():
    app = Flask(__name__) # Creating an instance of the Flask Application
    app.config.from_object(LocalDevelopmentConfig) # Setting the Configuration for the Flask Application
    db.init_app(app) # Initializing the Database with the Flask Application
    datastore = SQLAlchemyUserDatastore(db, User, Role) # Creating an instance of the SQLAlchemyUserDatastore
    app.security = Security(app, datastore) # Initializing the Security with the Flask Application and the SQLAlchemyUserDatastore
    app.app_context().push() # Pushing the Application Context
    return app


app = create_app() # Creating the Flask Application


# Main Function
if __name__ == '__main__':
    app.run() # Running the Flask Application