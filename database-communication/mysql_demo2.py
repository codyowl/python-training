import MySQLdb

db = MySQLdb.connect("localhost","root","root","testdb" )

cursor = db.cursor()

sql_command = "select * from testtable"

try:
   cursor.execute(sql_command)
   db.commit()
except:
   db.rollback()


db.close()