

import sqlite3

# Function to create the database and table
def create_table():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        marks REAL
    )
    """)
    connection.commit()
    connection.close()

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course name: ")
    marks = float(input("Enter marks: "))

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)", 
                   (name, age, course, marks))
    connection.commit()
    connection.close()
    print("✅ Student added successfully!\n")

# Function to view all students
def view_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n🎓 All Students:")
        print("-" * 50)
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}, Marks: {row[4]}")
        print("-" * 50)
    else:
        print("\n⚠️ No student records found.")
    connection.close()

# Function to search for a student by ID
def search_student():
    student_id = int(input("Enter student ID to search: "))
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row:
        print(f"\n🎯 Student Found → ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}, Marks: {row[4]}")
    else:
        print("\n⚠️ Student not found.")
    connection.close()

# Function to update a student's details
def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = float(input("Enter new marks: "))

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE students 
        SET name = ?, age = ?, course = ?, marks = ?
        WHERE id = ?
    """, (name, age, course, marks, student_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("✅ Student updated successfully!\n")
    else:
        print("⚠️ Student ID not found.\n")
    connection.close()

# Function to delete a student
def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("🗑️ Student deleted successfully!\n")
    else:
        print("⚠️ Student ID not found.\n")
    connection.close()

# Main Menu Loop
def main():
    create_table()  # Create table if it doesn’t exist
    while True:
        print("\n===== 🎓 STUDENT DATABASE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
