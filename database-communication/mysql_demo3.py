import MySQLdb

db = MySQLdb.connect("localhost","root","root","testdb" )

table_name = "table2"

cursor = db.cursor()

var1 = "firstthing2"
var2 = "middlething2"
var3 = "lastthing2"

# sql_query = "INSERT INTO table2 (name1, name2, name3) VALUES ('%s', '%s', '%s')" % (var1, var2, var3)

sql_query = "select * from %s" % (table_name)

print sql_query

cursor.execute(sql_query)

print "cursor execution done"