import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime  
import sql_sb

'''contains functions to fetch and plot data'''

def d_vs_S(query_dr):
    '''fetches date and sleep from daily_routine'''
    cnx = sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    s=[]
    for i in cursor.fetchall():
        d.append(np.datetime64(i[0]))
        s.append(int(i[1]))
    cursor.close()
    cnx.close()
    return d,s;

def d_vs_C(query_dr):
    '''fetches date and classes attended from daily_routine'''
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    c=[]
    for i in cursor.fetchall():
        d.append(np.datetime64(i[0]))
        c.append(int(i[1]))
    cursor.close()
    cnx.close()
    return d,c;

def d_vs_w(query_dr):
    '''fetches date and workout from daily_routine'''
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    w=[]
    for i in cursor.fetchall():
        d.append(np.datetime64(i[0]))
        w.append(int(i[1]))
    cursor.close()
    cnx.close()
    return d,w;

def d_vs_qos(query_dr):
    '''fetches date and quality of sleep from quality index'''
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    q=[]
    for i in cursor.fetchall():
        d.append(np.datetime64(i[0]))
        q.append(int(i[1]))
    cursor.close()
    cnx.close()
    return d,q;

def d_vs_oh(query_dr):
    '''this function fetches qualtiy of health and date from quality index'''
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    q=[]
    for i in cursor.fetchall():
        d.append(np.datetime64(i[0]))
        q.append(int(i[1]))
    cursor.close()
    cnx.close()
    return d,q;

def pro_plot():
    '''plots project infromation'''
    query_dr="SELECT PROJECT_NAME,HOURS_SPENT from project"
    cnx=sql_sb.connect_sql()
    cursor=cnx.cursor()
    sql_sb.connect_db(cursor)
    cursor.execute(query_dr)
    d=[]
    q=[]
    for i in cursor.fetchall():
        d.append((i[0]))
        q.append(int(i[1]))
    cursor.close()
    cnx.close()
    plt.bar(d,q)
    plt.show()

def plot_DvsQOS():
    ''''plots date vs qos'''
    query_dr="SELECT DATE, QOS from quality_index" 
    d,q=d_vs_qos(query_dr)
    print(d)
    plt.plot(d,q)
    plt.show()

def plot_DvsQOh():
    ''''plots date vs qos'''
    query_dr="SELECT DATE, OH from quality_index" 
    d,q=d_vs_oh(query_dr)
    print(d)
    plt.plot(d,q)
    plt.show()

def plot_DvsW():
    '''plots date vs workout'''
    query_dr="SELECT DATE,WORKOUT from daily_routine" 
    d,w=d_vs_w(query_dr)
    print(d)
    plt.plot(d,w)
    plt.show()

def plot_DvsC():
    '''plots date vs classes attended'''
    query_dr="SELECT DATE,CLASSES_ATTENDED from daily_routine" 
    d,c=d_vs_C(query_dr)
    print(d)
    plt.plot(d,c)
    plt.show()
 
def plot_DvsS():
    '''plots date vs sleep'''
    query_dr="SELECT DATE,HOURS_OF_SLEEP from daily_routine"
    d,s=d_vs_S(query_dr)
    print(d)
    plt.plot(d,s)
    plt.show()








