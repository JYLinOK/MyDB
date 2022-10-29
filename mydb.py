import mariadb

'''
time: 2022/10/29
author: Jinwei Lin
code name: mydb
version:0.0.1
'''


user_m = "root"
password_m = "123123"
host_m = "192.168.1.2"
port_m = 3306
database_m = ""

# _________________________________________________________________________________________________________________
# Connect a database
# T*
def connect_db(user, password, host, port, database):
    conn = mariadb.connect(user=user_m, password=password_m, host=host_m, port=port_m, database=database_m)
    cur = conn.cursor()
    return conn, cur


# _________________________________________________________________________________________________________________
# Execute a SQL code
# T*
def exe_SQL(cur, sql):
    cur.execute(sql)


# _________________________________________________________________________________________________________________
# Get result of a cur
# T*
def result_cur(cur, sql):
    return cur.fetchall()


# _________________________________________________________________________________________________________________
# Get result of a cur
# T*
def print_result_cur(cur, sql):
    print(cur.fetchall()) 


# _________________________________________________________________________________________________________________
# Close a db conn and cur
# T*
def close_db_cur_coon(cur, coon):
    cur.close()
    coon.close()
