from flask import Blueprint, jsonify
from data import users  # Importerar users-listan

router = Blueprint('router', __name__)

# ---- Routes ----
@router.route("/", methods=["GET"])
def home():
    return jsonify({"data": None})


@router.route("/api/users", methods=["GET"])
def get_all_users():
    return jsonify(users)


@router.route("/api/users/<uid>", methods=["GET"])
def get_user_by_uid(uid):
    user = users[int(uid) - 1]
    return jsonify(user)


@router.route("/api/users", methods=["POST"])
def add_user():
    new_user = {
        "uid": len(users) + 1,
        "name": request.form.get("name"),
        "mail": request.form.get("email"),
    }
    users.append(new_user)
    # return redirect("/api/users")
    return jsonify({"success": True})

@router.route("/api/users", methods=["PUT"])
def update_user():
    uid = int(request.form.get("uid"))
    user = users[uid-1]
    
    email = request.form.get("email").strip()
    name = request.form.get("name").strip()
    
    if name:
      user["name"] = name;
      
    if email:
      user["mail"] = email
      
    return jsonify({"success": True})

@router.route("/api/users", methods=["DELETE"])
def delete_user():
    uid = int(request.form.get("uid"))
    del users[uid - 1]

    return jsonify({"success": True})