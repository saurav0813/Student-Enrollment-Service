from flask import Flask, request, jsonify
from database import Database
import logging

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '9876',
    'host': 'localhost',
    'database': 'student_enrollment_db'  # Ensure this matches your schema name
}

database = Database(db_config)
logging.basicConfig(level=logging.DEBUG)

# API Endpoints

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    if not all(key in data for key in ('firstname', 'lastname', 'email', 'mobile_no', 'age', 'qualification')):
        return jsonify({'error': 'Missing fields'}), 400

    query = """
        INSERT INTO students (firstname, lastname, email, mobile_no, age, qualification)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    database.execute_query(query, (data['firstname'], data['lastname'], data['email'], data['mobile_no'], data['age'], data['qualification']))
    logging.info(f"Added student {data['firstname']} {data['lastname']}")
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/students', methods=['GET'])
def get_students():
    query = "SELECT * FROM students"
    students = database.fetch_query(query)
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    query = "SELECT * FROM students WHERE id = %s"
    student = database.fetch_query(query, (student_id,))
    if student:
        return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    query = """
        UPDATE students
        SET firstname = %s, lastname = %s, email = %s, mobile_no = %s, age = %s, qualification = %s
        WHERE id = %s
    """
    database.execute_query(query, (data['firstname'], data['lastname'], data['email'], data['mobile_no'], data['age'], data['qualification'], student_id))
    return jsonify({'message': 'Student updated successfully'}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"
    database.execute_query(query, (student_id,))
    return jsonify({'message': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

