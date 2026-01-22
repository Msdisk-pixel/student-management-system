# Student Management System
# Course: SEN 201

students = []

def add_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")

    student = {
        "name": name,
        "matric": matric
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("\nList of Students:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. Name: {student['name']}, Matric: {student['matric']}")
        print()

def main_menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()