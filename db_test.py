import os
import mysql.connector #lets me use sql in python 
from dotenv import load_dotenv

load_dotenv()

# opens the door/ connects me to my database
conn = mysql.connector.connect(  
host=os.getenv("DB_HOST"),
user=os.getenv("DB_USER"),
password= os.getenv("DB_PASS"),
database=os.getenv("DB_NAME")
)

#lets me access queries 
cursor = conn.cursor()  

# run query
cursor.execute("show tables;")
results = cursor.fetchall()
print(results)

#read from data 
cursor.execute("select id, username FROM users;")
rows = cursor.fetchall()

for row in rows:
    print (row)

#add data 
cursor.execute("insert into users (username) values (%s)", ("maria",))
conn.commit()
cursor.execute("select * from users;")
new_users = cursor.fetchall()
print (new_users)





#close the door/ exit database 
cursor.close()
conn.close()