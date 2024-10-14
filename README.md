# Student Enrollment System

A RESTful API built with Flask for managing student enrollment and records in a MySQL database. This system allows for CRUD operations on student data and provides a structured way to manage student information efficiently.

## Features

- **Add a Student**: Create a new student record.
- **Retrieve All Students**: Get a list of all enrolled students.
- **Retrieve a Specific Student**: Fetch details of a student by their ID.
- **Update Student Details**: Modify an existing student's information.
- **Delete a Student**: Remove a student record from the database.
- **Input Validation**: Ensure data integrity by validating required fields.

## Requirements

- Python 3.12.6
- Flask
- mysql-connector-python

## Setup

### 1. Clone the Repository

```bash
git clone <https://github.com/saurav0813/Student-Enrollment-Service>
cd </student-Enrollment-Service>

pip install Flask mysql-connector-python
db_config = {
    'user': 'root',
    'password': 'xxxx',
    'host': 'localhost',
    'database': 'student_enrollment_db'
}

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

python app.py

### Summary

This version includes all essential sections: project description, features, requirements, setup instructions, and how to run the application.
It’s clear and to the point, making it easy for anyone to understand how to get started with your project. Let me know if you need anything else!


