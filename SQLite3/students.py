import sqlite3
conn = sqlite3.connect("students.db")
c = conn.cursor()
# c.execute("CREATE TABLE students (person_id INTEGER, first_name TEXT, last_name TEXT, age INTEGER);")
# c.execute("INSERT INTO students VALUES (1, 'Andrei', 'Vodolazhchenko', 35);")
# insert_query = "INSERT INTO students VALUES (?, ?, ?, ?);"
# sum_list = [(2, 'Anna', 'Vodolazhchenko', 34), (3, 'Gleb', 'Vodolazhchenko', 1.8)]
# c.executemany(insert_query, sum_list)
c.execute("UPDATE students SET age = 20;")
c.execute("SELECT * FROM students;")
# print(c.fetchall())
for row in c:
    print(row)
conn.commit()
conn.close()
