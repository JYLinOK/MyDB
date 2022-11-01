import mariadb

'''
time: 2022/10/29
author: Jinwei Lin
code name: mydb
version:0.0.1
'''



# =================================================================================================================
# FUNCTIONS OPERATION
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
# Get the version of MariaDB
# T*
def get_version(cur):
    SQL(cur, sql_SELECT_VERSION())
    return cur.fetchall()




# _________________________________________________________________________________________________________________
# Create remote user
# T*
def SQL_create_remote_user(username, ip='%', password=''):
    sql = sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password(username, ip, password)
    return sql 



# =================================================================================================================





# =================================================================================================================
# TOOLS
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
# Delete the single quotes in a str
# T*
def delete_quotes_in_str(str):
    new_str = ''
    for char_i in str:
        if char_i not in ['\'', '"']:
            new_str += char_i
    return new_str



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
# Get str of a type value when it is used in a SQL code
# T*
def sql_str(value):
    if isinstance(value, str):
        return "'" + value + "'"
    else:
        return str(value)



# _________________________________________________________________________________________________________________
# Combine the chars list to a str
# T*
def combine_chars_to_aStr(chars_list):
    aStr = ''
    for char in chars_list:
        aStr += str(char)
    return aStr


# _________________________________________________________________________________________________________________
# Str a tuple
# T*
def strTuple(tuple):
    if not isinstance(tuple, str):
        return str(tuple)
    else:
        return "('" + str(tuple) + "')"




# =================================================================================================================





# =================================================================================================================
# SQL
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
# Get SQL code: get the version of MariaDB
# T*
def sql_SELECT_VERSION():
    return "SELECT VERSION();"



# _________________________________________________________________________________________________________________
# Get SQL code: DROP_TABLE_IF_EXISTS_MENU
# T*
def sql_DROP_TABLE_IF_EXISTS_table(table_name):
    return "DROP TABLE IF EXISTS " + str(table_name) + ";"



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
# Get SQL code: INSERT INTO tableName VALUES (...), (...), ...
# T*
def sql_INSERT_INTO_table_VALUES_tuples(db_name, table_name, tuple_list):
    values_str = str2DList_to_1d_tupleStr(tuple_list)
    sql = "use " + str(db_name) + "; " + "INSERT INTO " + str(table_name) + " VALUES " + values_str + ";"
    # print(f'{sql = }')
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tablename (field,field2,...) VALUES (value, value2,...);
# T*
def sql_INSERT_INTO_table_filedTuple_VALUES_valueTuples(db_name, table_name, filed_list, tuple_list):
    fileds_str_t = tuple(filed_list)
    # values_str = str2DList_to_1d_tupleStr(tuple_list)
    values_str_t = tuple(tuple_list)
    sql = "use " + str(db_name) + "; " + "INSERT INTO " + str(table_name) + " " + delete_quotes_in_str(str(fileds_str_t)) + " VALUES " + str(values_str_t) + ";"
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
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_DESC(db_name, column_list, table_name, order_lsit):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " DESC;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_ASC(db_name, column_list, table_name, order_lsit):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " ASC;"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: ELECT fileds, ... FROM Orders ORDER BY orders, ..., condiction
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_condiction(db_name, column_list, table_name, order_lsit, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table_name) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " " + str(condiction) + ";"
    print(sql)
    return sql 



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
# Get SQL code:  SELECT * FROM table LIMIT limit_num; 
# T*
def sql_SELECT_ALL_FROM_table_LIMIT_num(db_name, table_name, limit_num):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " LIMIT " + str(limit_num) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table LIMIT a,b; 
# T*
def sql_SELECT_ALL_FROM_table_LIMIT_a_to_b(db_name, table_name, a, b):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " LIMIT " + str(a-1) + "," + str(b-a+1) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str(x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE start with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_startWith_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str(x+'%') + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE end with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_endWith_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str('%'+x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE between x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_between_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str('%'+x+'%') + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE " + sql_str(x) + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE start with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_startWith_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE " + sql_str(x+'%') + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE end with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_endWith_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE " + sql_str('%'+x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE include x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_include_x(db_name, table_name, column, x):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE " + sql_str('%'+x+'%') + ";"
    print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE condiction
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_condiction(db_name, table_name, column, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str(condiction) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE condiction
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_condiction(db_name, table_name, column, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE " + sql_str(condiction) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE startWithLetters
# T
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_startWithLetters(db_name, table_name, column, letters_list):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE " + sql_str("[" + combine_chars_to_aStr(letters_list) + "]%")  + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE notstartWithLetters
# T
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_notStartWithLetters(db_name, table_name, column, letters_list):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE [!" + combine_chars_to_aStr(letters_list) + "]%;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE BINARY condiction
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_BINARY_condiction(db_name, table_name, column, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " LIKE BINARY '" + combine_chars_to_aStr(condiction) + "%';"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE BINARY condiction
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_BINARY_condiction(db_name, table_name, column, condiction):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT LIKE BINARY '" + combine_chars_to_aStr(condiction) + "%';"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column IN (tiems tuple)
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_IN_tuple(db_name, table_name, column, tuple):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " IN " + strTuple(tuple) + ";"
    # print(sql)
    return sql 




# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column IN (tiems tuple)
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_IN_tuple(db_name, table_name, column, tuple):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " NOT IN " + strTuple(tuple) + ";"
    # print(sql)
    return sql 




# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column BETWEEN a AND b
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_BETWEEN_a_AND_b(db_name, table_name, column, a, b):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(table_name) + " WHERE " + str(column) + " BETWEEN " + sql_str(a) + " AND " + sql_str(b) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column AS c FROM table 
# T*
def sql_SELECT_column_AS_c_FROM_table(db_name, column, c, table_name):
    sql = "use " + str(db_name) + "; " + "SELECT " + str(column)  + " AS " + str(c) + " FROM " + str(table_name) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column FROM table AS t
# T*
def sql_SELECT_column_FROM_table_AS_t(db_name, column, table_name, t):
    sql = "use " + str(db_name) + "; " + "SELECT " + str(column)  + " FROM " + str(table_name) + " AS " + str(t) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column AS c FROM table AS t
# T*
def sql_SELECT_column_AS_c_FROM_table_AS_t(db_name, column, c, table_name, t):
    sql = "use " + str(db_name) + "; " + "SELECT " + str(column)  + " AS " + str(c) +  " FROM " + str(table_name) + " AS " + str(t) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta [inner] JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_INNER_JOIN_tb_ON_taKey_equal_tbKey(db_name, ta, tb, key):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(ta) + " INNER JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta LEFT JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey(db_name, ta, tb, key):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta FULL JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_FULL_JOIN_tb_ON_taKey_equal_tbKey(db_name, ta, tb, key):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(ta) + " FULL JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta FULL OUTER JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_FULL_OUTER_JOIN_tb_ON_taKey_equal_tbKey(db_name, ta, tb, key):
    sql = "use " + str(db_name) + "; " + "SELECT * FROM " + str(ta) + " FULL OUTER JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 