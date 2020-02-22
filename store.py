import mysql.connector
import insert_data as i_d

mydb = mysql.connector.connect(
  host="localhost",
  user="manav",
  passwd="zxcv@1234"
)
mycursor.execute("CREATE DATABASE sql project")
mycursor = mydb.cursor()
mysql.execute()
mycursor.execute("USE Newdb")



sql_command = """CREATE TABLE IF NOT EXISTS Test (h1 INT,
h2 INT,
h3 INT,
h4 INT,
h5 INT,
h6 INT,
h7 INT)"""


mycursor.execute(sql_command)

dic=i_d.inputw()

i1 = dic['g1']
i2 = dic['g2']
i3 = dic['g3']
i4 = dic['g4']
i5 = dic['g5']
i6 = dic['g6']
i7 = dic['g7']

sql_command = """INSERT INTO Test (h1, h2, h3, h4, h5, h6, h7) VALUES (i1, i2, i3, i4, i5, i6, i7)"""

mycursor.execute(sql_command)

mydb.commit()

mycursor.execute("SELECT* FROM Test")

myresult=mycursor.fetchall()

for r in myresult:
	print(r)