from application.database import db
from flask_security import UserMixin, RoleMixin

# User Model
class User(db.Model, UserMixin):
    # common fields for both user and admin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(255), nullable=False) # Unique Identifier(Token) for Flask Security to allow user to access endpoints based on their roles
    # user fields
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=True)
    qualification = db.Column(db.String(255), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    # activity - active or inactive (user)
    active = db.Column(db.Boolean, nullable=False) # By default value is True
    created_at = db.Column(db.DateTime, nullable=False)
    # relationship with roles
    roles = db.relationship('Role', secondary='users_roles', backref=db.backref('users', lazy='dynamic')) # All roles associated with the user


# Role Model
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)


# UsersRoles Model - many to many relationship between User and Role
class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))