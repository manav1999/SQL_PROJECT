import mysql.connector 
from mysql.connector import errorcode

def connect_sql():
    '''connects to sql server returns cnx if successful else returns none '''
    config={'user':'manav','password':'zxcv@1234','host':'127.0.0.1'}
    try:
        cnx=mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
         else:
            print(err)
         return None



def connect_db(cursor):
    '''connects to database ,if database doesn't exisit it calles create_db , accepts cursor as an argument'''
    try:
        cursor.execute("USE {}".format("sqlproject"))
        print("using db")
    except mysql.connector.Error as err:
        print("Database {} does not exists".format("sqlproject"))
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            create_db(cursor)
            print("Database {} created successfully ".format("sqlpriject"))
            
        else:
            print(err)
            
            
def create_db(cursor):
    '''creates database '''
    
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format("sqlproject"))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)    

