from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"}
]


@app.route("/")
def index():
    return "Hello World"


# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# Route to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201


# Route to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"}), 204


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
