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
    conn = mariadb.connect(user, password, host, port, database, database)
    cur = conn.cursor()
    return conn, cur



# _________________________________________________________________________________________________________________
# Split a str in list by split list, return a str splited by enter char
def split_str_by_spList_ret_enterStr(str, split_list):
    new_str = ''
    for char_i in str:
        if char_i != '\n' and char_i in split_list:
            char_i = '\n'
        new_str += char_i
    return new_str

   


# _________________________________________________________________________________________________________________
# Split a str in list by split list, return a str splited list
def split_str_by_spList_ret_list(str, split_list):
    new_str = ''
    for char_i in str:
        if char_i != '\n' and char_i in split_list:
            char_i = '\n'
        new_str += char_i
    return new_str.split('\n')




# _________________________________________________________________________________________________________________
# Execute a SQL code
# Add: execute multiple line code function
# T*
def SQL(cur, sql):
    not_enter_strList = []
    if '\n' in sql:
        for str_i in sql.pli

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
def sql_SELECT_VERSION():
    return "SELECT VERSION();"



# _________________________________________________________________________________________________________________
# Get the version of MariaDB
# T*
def get_version(cur):
    SQL(cur, sql_SELECT_VERSION())
    return cur.fetchall()



# _________________________________________________________________________________________________________________
# Get SQL code: DROP_TABLE_IF_EXISTS_MENU
# T*
def sql_DROP_TABLE_IF_EXISTS_tableName(table_name):
    return "DROP TABLE IF EXISTS " + str(table_name) + ";"


# _________________________________________________________________________________________________________________
# Get SQL code: CREATE TABLE table_name(table_detail_list)
# T*
def sql_CREATE_TABLE_tableName(table_name, table_detail_list):
    return "DROP TABLE IF EXISTS " + str(table_name) + ";"
