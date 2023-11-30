# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Endpoint for updating employee image
# @app.route('/upload/image', methods=['POST'])
# def upload_image():
#     data = request.json
#     image_src = data.get('imageSrc')

#     # Save the image or process it as needed
#     # For simplicity, let's print the base64-encoded image data
#     print('Received image:', image_src)

#     return jsonify({'status': 'success', 'message': 'Image uploaded successfully'}), 200

# # Endpoint for updating user location
# @app.route('/update/location', methods=['POST'])
# def update_location():
#     data = request.json
#     latitude = data.get('latitude')
#     longitude = data.get('longitude')

#     # Process the location data as needed
#     print('Received location:', latitude, longitude)

#     return jsonify({'status': 'success', 'message': 'Location updated successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to MongoDB using your connection string
# Replace 'your_connection_string' with your actual MongoDB connection string
# Example: 'mongodb+srv://<username>:<password>@cluster0.yfliaq8.mongodb.net/<database_name>?retryWrites=true&w=majority'
mongodb_connection_string = 'mongodb+srv://purushoth170288:Bruce17@cluster0.yfliaq8.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongodb_connection_string)
db = client['test']  # Replace 'your_database_name' with your actual database name
employee_collection = db['employees']
admin_collection = db['admins']
# Example structure for an employee document
employee_document = {
    'id': 'employee123',
    'username': 'employee_username',
    'password': generate_password_hash('employee_password'),
    # Add other fields as needed
}

# Insert the employee document into the collection
employee_collection.insert_one(employee_document)

# Example structure for an admin document
admin_document = {
    'id': 'admin123',
    'username': 'admin_username',
    'password': generate_password_hash('admin_password'),
    # Add other fields as needed
}

# Insert the admin document into the collection
admin_collection.insert_one(admin_document)


# Endpoint for updating employee image
@app.route('/upload/image', methods=['POST'])
def upload_image():
    data = request.json
    image_src = data.get('imageSrc')

    # Save the image or process it as needed
    # For simplicity, let's print the base64-encoded image data
    print('Received image:', image_src)

    return jsonify({'status': 'success', 'message': 'Image uploaded successfully'}), 200

# Endpoint for updating user location
@app.route('/update/location', methods=['POST'])
def update_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Process the location data as needed
    print('Received location:', latitude, longitude)

    return jsonify({'status': 'success', 'message': 'Location updated successfully'}), 200

# Endpoint for employee login
@app.route('/login/employee', methods=['POST'])
def employee_login():
    data = request.json
    employee = employee_collection.find_one({'id': data['id']})

    if employee and check_password_hash(employee['password'], data['password']):
        return jsonify({'status': 'success', 'message': 'Employee login successful'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

# Endpoint for admin login
@app.route('/login/admin', methods=['POST'])
def admin_login():
    data = request.json
    admin = admin_collection.find_one({'id': data['id']})

    if admin and check_password_hash(admin['password'], data['password']):
        return jsonify({'status': 'success', 'message': 'Admin login successful'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401
# Endpoint for viewing employee image
@app.route('/view/image', methods=['POST'])
def view_image():
    data = request.json
    employee_id = data.get('employeeId')

    # Fetch the employee image URL or data based on the employee ID
    # For simplicity, let's assume the image URL is stored in the database
    employee = employee_collection.find_one({'id': employee_id})

    if employee and 'image_url' in employee:
        return jsonify({'status': 'success', 'imageSrc': employee['image_url']}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)