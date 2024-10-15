# Student Enrollment System

A RESTful API built with Flask for managing student enrollment and records in a MySQL database. This system allows for CRUD operations on student data and provides a structured way to manage student information efficiently.

## Features

- **Add a Student**: Create a new student record.
- **Retrieve All Students**: Get a list of all enrolled students.
- **Retrieve a Specific Student**: Fetch details of a student by their ID.
- **Update Student Details**: Modify an existing student's information.
- **Delete a Student**: Remove a student record from the database.
- **Requirements
Input Validation**: Ensure data integrity by validating required fields.

## 
- Python 3.12.6
- Flask
- mysql-connector-python

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sauravkrgautam/Student-Enrollment-Service
cd /student-Enrollment-Service
```
### 2. Install Dependencies
```bash
pip install Flask mysql-connector-python
```
### 3.Database Setup
```sql
CREATE DATABASE student_enrollment_db;

USE student_enrollment_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(100),
    mobile_no VARCHAR(15),
    age INT,
    qualification VARCHAR(100)
);
```
### 4. Configure Database Connection
```python
db_config = {
    'user': 'root',
    'password': xxxx,
    'host': 'localhost',
    'database': 'student_enrollment_db'
}
```
### 5. Run the application
```bash
python app.py
```
## Summary
This README provides all essential sections: project description, features, requirements, setup instructions, and how to run the application. 
It serves as a guide for users and contributors, facilitating easier onboarding and understanding of the project's functionality.

## License

### Notes:
- Replace `xxxx` with your actual MySQL password.
- Ensure that the commands and instructions are accurate for your specific setup.
- Feel free to customize any part of this README to better fit your style or additional details about your project!
