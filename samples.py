import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "mike213" , hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john" , hashlib.sha256("mycatisgreat777".encode()).hexdigest()
username3, password3 = "strike999" , hashlib.sha256("ILikeStriking".encode()).hexdigest()
username4, password4 = "neuralnine" , hashlib.sha256("neuralpassword".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

#print(password2)

conn.commit()



