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
    app.app_context().push() # Pushing the Application Context (Connecting everyting to the Flask Application)
    return app


app = create_app() # Creating the Flask Application

with app.app_context(): # Application Context
    db.create_all() # Creating the Database Tables if not present ( This will not create the tables if they are already present)

    # Creating Roles
    app.security.datastore.find_or_create_role(name="admin", description="Superuser of the app") # Creating a Role - Admin
    app.security.datastore.find_or_create_role(name="user", description="General user of the app") # Creating a Role - User
    db.session.commit() # Committing the Changes to the Database

    # Check if the Admin User is present in the Database
    if not app.security.datastore.find_user(email="admin@quizmaster.com"):
        # Creating the Admin User
        app.security.datastore.create_user(
            email="admin@quizmaster.com", 
            password="admin@123", 
            firstname="Admin", 
            active=True, 
            roles=["admin"]
        )


# Main Function
if __name__ == '__main__':
    app.run() # Running the Flask Application