import pymysql

port = 3386
user = "root"
pw = "root"
db_name="fencegate"

db = pymysql.connect("localhost:"+port, user, pw, db_name)

cursor = db.cursor()

