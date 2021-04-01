import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT)"
users_list = [
    ('Andrei123', 'qwerty'),
    ('Anna456', 'asdfg')
]
# insert_query = "INSERT INTO users VALUES (?, ?)"
name = input('Enter name: ')
password = input('Enter password: ')
select_query = f"SELECT * FROM users WHERE user_name = '{name}' AND user_password = '{password}'"
# c.executemany(insert_query, users_list)
c.execute(select_query)
a = c.fetchone()
if a:
    print("Good")
else:
    print("Bad")
conn.commit()
conn.close()
