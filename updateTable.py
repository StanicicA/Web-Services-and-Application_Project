import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="wsaa"
)

cursor = db.cursor()
sql="update student2 set firstname= %s, age=%s  where id = %s"
values = ("Ian",35, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()