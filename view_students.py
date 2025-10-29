import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("🎓 Student Records:")
for row in rows:
    print(row)

connection.close()
