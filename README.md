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
git clone https://github.com/saurav0813/Student-Enrollment-Service
cd /student-Enrollment-Service```

### 2.Install Dependencies
```bash
pip install Flask mysql-connector-python```

### 3. Configure the Database
```python
db_config = {
    'user': 'root',
    'password': '9876', 
    'host': 'localhost',
    'database': 'student_enrollment_db'
}```

### 4. Create the Database
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
);```
### 5. Run the Application
```bash
python app.py ```

### Summary
```vbnet
This version clearly separates each step and uses proper formatting for code blocks. It specifies where to replace the password and emphasizes running commands in the correct environments. This should make it easy for users to follow your setup instructions. Let me know if you need any more changes!







