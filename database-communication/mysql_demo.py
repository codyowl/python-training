import MySQLdb

db = MySQLdb.connect("localhost","root","root","testdb" )

cursor = db.cursor()

query_executer = cursor.execute("select * from testtable")

# print cursor.fetchone()

print cursor.fetchall()