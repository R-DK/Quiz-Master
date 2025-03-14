from application.database import db


class User(db.Model):
    # common fields for both user and admin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fs_uniqifier = db.Column(db.String(255), nullable=False) # Unique Identifier(Token) for Flask Security to allow user to access endpoints based on their roles
    # user fields
    firstname = db.Column(db.String(255), nullable=True)
    lastname = db.Column(db.String(255), nullable=True)
    qualification = db.Column(db.String(255), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    # activity - active or inactive (user)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    # Check if current user is an Admin  or not
    is_admin = db.Column(db.Boolean, nullable=False)