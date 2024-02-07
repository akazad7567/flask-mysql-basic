# app.py

from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)

# Update user data
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        db = Database()
        db.update_user(user_id, data)
        db.close_connection()
        return jsonify({'message': 'User data updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get user data by user_id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        db = Database()
        user_data = db.get_user(user_id)
        db.close_connection()
        if user_data:
            return jsonify(user_data), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        db = Database()
        user_id = db.create_user(data)
        db.close_connection()
        return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
