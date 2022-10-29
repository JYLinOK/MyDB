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
    conn = mariadb.connect(user, password, host, port, database)
    cur = conn.cursor()
    return conn, cur


# _________________________________________________________________________________________________________________
# Connect a database with dict
# T*
def connect_db_d(d):
    conn = mariadb.connect(user=d["user"], password=d["password"], host=d["host"], port=d["port"], database=d["database"])
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
# Execute a SQL code
# Add: execute multiple line code function
# T*
def SQL_noResult(cur, sql):
    sql_code_list = []
   
    if isinstance(sql, str):
        sql_code_list = sql.split(";")
        # print(f'1: {sql_code_list = }')

    elif isinstance(sql, list):
        sql_code_list = sql
        # print(f'2: {sql_code_list = }')

    for sql_i in sql_code_list:
        if sql_i != '':
            cur.execute(sql_i.strip())



# _________________________________________________________________________________________________________________
# Execute a SQL code
# Add: execute multiple line code function
# T*
def SQL(cur, sql):
    sql_code_list = []
    if isinstance(sql, str):
        sql_code_list = sql.split(";")
        # print(f'1: {sql_code_list = }')
    elif isinstance(sql, list):
        sql_code_list = sql
        # print(f'2: {sql_code_list = }')

    for sql_i in sql_code_list:
        if sql_i != '':
            try:
                cur.execute(sql_i.strip() + ";")
                return cur.fetchall()
            except:
                pass
    


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
def sql_DROP_TABLE_IF_EXISTS_table(table_name):
    return "DROP TABLE IF EXISTS " + str(table_name) + ";"



# _________________________________________________________________________________________________________________
# Add items of a list to be a big str
def one_str_from_strList(strList, add_char=","):
    one_str = ''

    for i in range(len(strList)):
        str_i = strList[i]
        if i < len(strList)-1 and str_i.strip()[-1] != ",": 
            str_i += ","
        elif i == len(strList)-1 and str_i.strip()[-1] == ",": 
            str_i = str_i[:-1]
        one_str += str_i

    return one_str


# _________________________________________________________________________________________________________________
# Get SQL code: SHOW TABLES;
# T*
def sql_SHOW_TABLES(db_name):
    sql = "use " + str(db_name) + "; SHOW TABLES;"
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: CREATE TABLE table_name(table_detail_list)
# T*
def sql_CREATE_TABLE_use_db_create_table(db_name, table_name, table_detail):
    sql = ''
    str_table_detail = ''
    if isinstance(table_detail, str):
        str_table_detail = table_detail
    elif isinstance(table_detail, list):
        str_table_detail = one_str_from_strList(table_detail)
        
    sql = "use " + str(db_name) + "; " + "CREATE TABLE " + str(table_name) + "(" + str_table_detail + ");"
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DROP TABLE tableName
# T*
def sql_DROP_TABLE(db_name, table_name):
    sql = "use " + str(db_name) + "; " + "DROP TABLE " + str(table_name) + ";"
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: DESCRIBE tableName;
# T*
def sql_DESCRIBE_tableName(db_name, table_name):
    sql = "use " + str(db_name) + "; " + "DESCRIBE " + str(table_name) + ";"
    print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SHOW COLUMNS FROM tableName
# T*
def sql_SHOW_COLUMNS_FROM_table(db_name, table_name):
    sql = "SHOW COLUMNS FROM " + str(table_name) + " FROM " +  str(db_name) + ";"
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM tableName
# T*
def sql_SELECT_ALL_FROM_table(db_name, table_name):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + ";"
    return sql 




