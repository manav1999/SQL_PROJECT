import sql_sb
import mysql.connector
from mysql.connector import errorcode

def create_tables(tables):
    
    cnx=sql_sb.connect_sql()
    if cnx is None:
        print("unable to execute connect_sql")
    else:
        cursor=cnx.cursor()
        sql_sb.connect_db(cursor)
        for t_names in tables:
            t_dis=tables[t_names]
            try:
                #print('Creating table {}'.format(t_names),end=" ")
                cursor.execute(t_dis)
            except mysql.connector.Error as err:
                if err.err == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("table already exists.")
                else:
                    print(err.msg)
    cursor.close()
    cnx.close()            

