from flask import current_app as app  # use the app object created in the app.py file
from application.database import db
from flask import jsonify, request
from flask_security import auth_required, roles_required, hash_password
from datetime import datetime


@app.route('/api/register', methods=["POST"])
def register():
    data = dict(request.get_json())
    if not data or not {"email", "password", "firstname", "qualification"}.issubset(data.keys()):
        return jsonify({"message": "Invalid Data"}), 400
    if app.security.datastore.find_user(email=data["email"]):
        return jsonify({"message": "User already exists"}), 400
    app.security.datastore.create_user(
        email=data["email"],
        password=hash_password(data["password"]),
        firstname=data.get("firstname"),
        active=True,
        roles=["user"],
        created_at=datetime.now()
    )

    db.session.commit()
    return jsonify({"message": "User Created"}), 201


@app.route('/api/admin')
@auth_required('token')  # this decorator ensures that the user is authenticated
@roles_required('admin')  # this decorator ensures that the user has the 'admin' role (RBAC)
def admin_home():
    return jsonify({"message": "Welcome Admin!"})