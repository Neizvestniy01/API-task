from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Asberit", "email": "john@gmail.com"},
    {"id": 2, "name": "Michael Kavori", "email": "michael@gmail.com"},
    {"id": 3, "name": "Alice Smith", "email": "alice@gmail.com"},
    {"id": 4, "name": "Bob Johnson", "email": "bob@gmail.com"},
    {"id": 5, "name": "Charlie Brown", "email": "charlie@gmail.com"}
]

@app.route("/api/GetUsers", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/PostUsers", methods=["POST"])
def create_user():
    new_user = request.json
    new_user["id"] = max([u["id"] for u in users], default=0) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/api/PatchUsers/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            user.update(request.json)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/api/DeleteUsers/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)