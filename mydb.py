import mariadb

'''
time: 2022/10/29
author: Jinwei Lin
code name: mydb
version:0.0.1
'''


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
def SQL(cur, sql):
    cur.execute(sql)


# _________________________________________________________________________________________________________________
# Get result of a cur
# T*
def result_cur(cur):
    return cur.fetchall()


# _________________________________________________________________________________________________________________
# Get result of a cur
# T*
def print_result_cur(cur):
    print(cur.fetchall()) 


# _________________________________________________________________________________________________________________
# Close a db conn and cur
# T*
def close_db_cur_coon(cur, coon):
    cur.close()
    coon.close()


# _________________________________________________________________________________________________________________
# Get SQL code: get the version of MariaDB
# T*
def sql_get_version():
    return "SELECT VERSION();"


# _________________________________________________________________________________________________________________
# Get the version of MariaDB
# T*
def get_version(cur):
    SQL(cur, sql_get_version())
    return cur.fetchall()