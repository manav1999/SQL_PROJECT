from __future__ import print_function
import insert_data
import mysql.connector
import sql_sb
''' functions to insert user data into sql'''

def push_Data(field,data):
    ''' push data to sql'''
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(field,data)
    cnx.commit()
    cursor.close()
    cnx.close()

def qualtiy_insert():
    '''insert qality data quality index sql'''
    data=insert_data.quality_Index()
    add_e=("INSERT INTO quality_index"
    "(QOS,OH,COMMENT,DATE)"
    "VALUES(%(QOS)s,%(OH)s,%(COMMENT)s,%(DATE)s)")
    data_list=['QOS','OH','COMMENT','DATE']
    dic_data={data_list[i]:data[i] for i in range(len(data_list))}
    print(dic_data)
    push_Data(add_e,dic_data)
    
def daily_insert():
    '''inserts data into daily routine table table'''
    data=insert_data.daily_routine()
    add_e = ("INSERT INTO DAILY_ROUTINE"
            "(Date, hours_of_sleep, classes_attended, workout , weekend)"
            "VALUES (%(DATE)s,%(HOURS_OF_SLEEP)s,%(CLASSES_ATTENDED)s,%(WORKOUT)s,%(WEEKEND)s)")
    data_list=['DATE','HOURS_OF_SLEEP','CLASSES_ATTENDED','WORKOUT','WEEKEND']
    dic_data={data_list[i]:data[i] for i in range(len(data_list))}
    print(dic_data)
    print("new row added to insert_data")
    push_Data(add_e,dic_data)

def project_insert():
    '''inserts data into project table'''
    name,hours=insert_data.project()
    print(name,hours)
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    p_id,check=check_pid(cursor,name)
    if check:
        query=("UPDATE project SET HOURS_SPENT=HOURS_SPENT + %s ")
        cursor.execute(query,(hours,))
        cnx.commit()
        cnx.close()
        cursor.close()
    else:
        data=[p_id,name,hours]
        add_e=("INSERT INTO project"
        "(PROJECT_ID,PROJECT_NAME,HOURS_SPENT)"
        "VALUES(%(PROJECT_ID)s,%(PROJECT_NAME)s,%(HOURS_SPENT)s)")
        data_list=['PROJECT_ID','PROJECT_NAME','HOURS_SPENT']
        dic_data={data_list[i]:data[i] for i in range(len(data_list))}
        push_Data(add_e,dic_data)  
    
def check_pid(cursor,name):
    ''' this functions checks if the project already exist'''
    query=("Select PROJECT_ID FROM project WHERE PROJECT_NAME = %s")
    cursor.execute(query,(name,))
    a=cursor.fetchall()
    if a:
        return a[0][0],True;
    else:
        return insert_data.pid_generate(name),False;
    
def daily_input():
    '''calls all the insert fucn'''
    print("Enter quality Index")
    qualtiy_insert()
    print("Enter daily input")
    daily_insert()
    print("Enter Project info")
    project_insert()








