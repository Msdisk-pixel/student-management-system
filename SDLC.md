Name: Uwaoma Donald Chiedozie.              Matric:24/15192
Department: Computer science.                    Level:200

Course code: SEN 201
 Project Title: Student Management System 

SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
FOR STUDENT MANAGEMENT SYSTEM**
1. Introduction
The Student Management System is a simple Python-based application developed to manage student records.
The system allows users to add student information and view stored student records through a command-line interface.
This project follows the Software Development Life Cycle (SDLC) to ensure proper planning, design, development, testing, deployment, and maintenance of the system.
2. Requirement Analysis
The requirement analysis stage identifies what the Student Management System is expected to do.
Functional Requirements
The system shall allow the user to add a student.
The system shall allow the user to view all students.
Each student record shall contain:
Student Name
Matric Number
Non-Functional Requirements
The system shall be easy to use.
The system shall be written using Python.
The system shall run on a command-line interface.
The system shall respond quickly to user input.
3. System Design
This stage explains how the Student Management System will be structured and how it will operate.
System Architecture
The system is a console-based application.
Python is used as the programming language.
Data Design
Student records are stored using a list of dictionaries.
Each dictionary represents one student.
Example data structure:
Copy code
Python
students = [
    {"name": "John Doe", "matric": "SEN201001"}
]
Program Flow
Display a menu with options:
Add Student
View Students
Exit
User selects an option.
The system performs the selected operation.
The menu is displayed again until the user exits.
4. Implementation
This stage involves writing the actual code for the Student Management System.
Implementation Details
Programming Language: Python
File Name:
Copy code

student_management_system.py
Modules and Functions
add_student() – Adds a new student to the system.
view_students() – Displays all stored students.
main_menu() – Displays menu options and controls program flow.
The implementation was carried out using a Python development environment, and the program runs successfully on the command line.
5. Testing
Testing ensures that the Student Management System works correctly and meets its requirements.
Testing Method
Manual testing was used.
Test Cases
Test Case
Expected Result
Add a student
Student is added successfully
View students
All students are displayed
Exit program
Program closes properly
All test cases were executed successfully, and the system behaved as expected.
6. Deployment
Deployment is the stage where the completed system is made available for use.
The Student Management System was deployed by uploading the source code to GitHub.
Repository Name:
Copy code

student-management-system
The Python file student_management_system.py was uploaded to the repository.
The GitHub repository link will be submitted as required.
7. Maintenance
Maintenance involves future improvements and updates to the system.
Possible Future Enhancements
Ability to delete student records.
Ability to update student information.
Permanent storage using files or a database.
Adding user authentication.
These improvements can be implemented in future versions of the system.
8. Conclusion
The Student Management System was successfully developed using the Software Development Life Cycle (SDLC).
The system meets all defined requirements and provides a simple and effective way to manage student records using Python.

