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
    elif isinstance(sql, list):
        sql_code_list = sql

    for sql_i in sql_code_list:
        if sql_i != '':
            try:
                # print(f'{sql_i = }')
                cur.execute(sql_i.strip() + ";")
                return cur.fetchall()
            except Exception as e:
                # print(f'SQL:{e = }')
                pass
    


# _________________________________________________________________________________________________________________
# Execute a SQL code with commit
# Add: execute multiple line code function
# T*
def SQLcommit(cur, conn, sql):
    sql_code_list = []
    if isinstance(sql, str):
        sql_code_list = sql.split(";")
    elif isinstance(sql, list):
        sql_code_list = sql

    for sql_i in sql_code_list:
        if sql_i != '':
            try:
                # print(f'{sql_i = }')
                cur.execute(sql_i.strip() + ";")
                conn.commit()
                return cur.fetchall()
            except Exception as e:
                # print(f'SQL:{e = }')
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
def str2DList_to_1str(strList, add_char=","):
    one_str = ''

    for i in range(len(strList)):
        str_i = strList[i]
        if i < len(strList)-1 and str_i.strip()[-1] != add_char: 
            str_i += ","
        elif i == len(strList)-1 and str_i.strip()[-1] == add_char: 
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
        str_table_detail = str2DList_to_1str(table_detail)
        
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
def sql_DESCRIBE_table(db_name, table_name):
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



# _________________________________________________________________________________________________________________
# 2D list to 1d tuple str
# T*
def str2DList_to_1d_tupleStr(str2DList):
    tupleStr = ''
    for i in range(len(str2DList)):
        tuple_i_str = ''
        if isinstance(str2DList[i], tuple):
            tuple_i_str = str(str2DList[i])
        elif isinstance(str2DList[i], list):
            tuple_i_str = str(tuple(str2DList[i]))

        if i < len(str2DList)-1:
            tupleStr += tuple_i_str + ','
        else:
            tupleStr += tuple_i_str
    return tupleStr



# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tableName VALUES (...), (...), ...
# T*
def sql_INSERT_INTO_table_VALUES_tuples(db_name, table_name, tuple_list):
    values_str = str2DList_to_1d_tupleStr(tuple_list)
    sql = "use " + str(db_name) + "; " + "INSERT INTO " + str(table_name) + " VALUES " + values_str + ";"
    # print(f'{sql = }')
    return sql 



# _________________________________________________________________________________________________________________
# Delete the single quotes in a str
# T*
def delete_single_quotes_in_str(str):
    new_str = ''
    for char_i in str:
        if char_i not in ['\'', '"']:
            new_str += char_i
    return new_str



# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tablename (field,field2,...) VALUES (value, value2,...);
# T*
def sql_INSERT_INTO_table_filedTuple_VALUES_valueTuples(db_name, table_name, filed_list, tuple_list):
    fileds_str_t = tuple(filed_list)
    # values_str = str2DList_to_1d_tupleStr(tuple_list)
    values_str_t = tuple(tuple_list)
    sql = "use " + str(db_name) + "; " + "INSERT INTO " + str(table_name) + " " + delete_single_quotes_in_str(str(fileds_str_t)) + " VALUES " + str(values_str_t) + ";"
    print(f'{sql = }')
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: CREATE USER 'username' @ 'localhost' IDENTIFIED BY 'password';
# T*
def sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password(username, ip='localhost', password=''):
    sql = "CREATE USER '" + str(username) + "'@'" + str(ip) + "' IDENTIFIED BY '" + str(password) + "';"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Create remote user
# T*
def SQL_create_remote_user(username, ip='%', password=''):
    sql = sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password(username, ip, password)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column FROM tableName
# T*
def sql_SELECT_column_FROM_table(db_name, column_list, table_name):
    column_list_str = ''
    for i in range(len(column_list)):
        if i < len(column_list)-1:
            column_list_str += column_list[i].strip() + ','
        else:
            column_list_str += column_list[i].strip()

    sql = "use " + str(db_name) + "; " + "SELECT " + str(column_list_str) + " FROM " + str(table_name) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT [column_list] FROM tableName
# T*
def sql_SELECT_columnList_FROM_table(db_name, column_list, table_name):
    return sql_SELECT_column_FROM_table(db_name, column_list, table_name) 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT DISTINCT column FROM tableName
# T*
def sql_SELECT_DISTINCT_column_FROM_table(db_name, column_list, table_name):
    column_list_str = ''
    for i in range(len(column_list)):
        if i < len(column_list)-1:
            column_list_str += column_list[i].strip() + ','
        else:
            column_list_str += column_list[i].strip()
    sql = "use " + str(db_name) + "; " + "SELECT DISTINCT " + str(column_list_str) + " FROM " + str(table_name) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT DISTINCT [column_list] FROM tableName
# T*
def sql_SELECT_DISTINCT_columnList_FROM_table(db_name, column_list, table_name):
    return sql_SELECT_DISTINCT_column_FROM_table(db_name, column_list, table_name) 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM tableName WHERE condiction
# T*
def sql_SELECT_ALL_FROM_table_WHERE_condiction(db_name, table_name, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(condiction) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ...
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList(db_name, column_list, table_name, order_lsit):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_single_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_single_quotes_in_str(str(order_lsit))[1:-1] + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_DESC(db_name, column_list, table_name, order_lsit):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_single_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_single_quotes_in_str(str(order_lsit))[1:-1] + " DESC;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_ASC(db_name, column_list, table_name, order_lsit):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_single_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_single_quotes_in_str(str(order_lsit))[1:-1] + " ASC;"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: ELECT fileds, ... FROM Orders ORDER BY orders, ..., condiction
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_condiction(db_name, column_list, table_name, order_lsit, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_single_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_single_quotes_in_str(str(order_lsit))[1:-1] + " " + str(condiction) + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Change key-value list to kv str
# T*
def kvList_2_kvStr(kv_list):
    kvStr = ''
    for i in range(len(kv_list)):
        k_v = kv_list[i]
        k = str(k_v[0])
        if isinstance(k_v[1], str):
            v = "'" + str(k_v[1]) + "'"
        else:
            v = str(k_v[1])
        if i < len(kv_list)-1:
            kvStr += k + ' = ' + v + ','
        else:
            kvStr += k + ' = ' + v
    return kvStr



# _________________________________________________________________________________________________________________
# Get SQL code: UPDATE table SET column_kv_list WHERE column_conkv_list
# T*
def sql_UPDATE_table_SET_columnKvlist_WHERE_columnConkvList(db_name, table_name, column_kv_list, column_conkv_list):
    sql = "use " + str(db_name) + "; " + "UPDATE " + str(table_name) + " SET " + kvList_2_kvStr(column_kv_list) + " WHERE " + kvList_2_kvStr(column_conkv_list) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DELETE FROM table WHERE k=v
# T*
def sql_DELETE_FROM_table_WHERE_kv(db_name, table_name, column_conkv):
    sql = "use " + str(db_name) + "; " + "DELETE FROM " + str(table_name) + " WHERE " + kvList_2_kvStr([column_conkv]) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DELETE * FROM table 
# T*
def sql_DELETE_ALL_FROM_table_WHERE_kv(db_name, table_name):
    sql = "use " + str(db_name) + "; " + "DELETE * FROM " + str(table_name) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT TOP num * FROM table
# T*
def sql_SELECT_TOP_num_ALL_FROM_table(db_name, num, table_name):
    sql = "use " + str(db_name) + "; " + "SELECT TOP " + str(num) + " * FROM " + str(table_name) + ";"
    print(sql)
    return sql 











