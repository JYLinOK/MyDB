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
# Get the Constraints of SQL
# T*
def get_Constraints():
    return [
        "NOT NULL",
        "UNIQUE",
        "PRIMARY KEY",
        "FOREIGN KEY",
        "CHECK",
        "DEFAULT",
    ]



# _________________________________________________________________________________________________________________
# Create remote user
# T*
def SQL_create_remote_user(username, ip='%', password=''):
    sql = sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password(username, ip, password)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL str datatype
# T*
def get_str_datatype():
    return [
        "CHAR(size): 0-255",
        "VARCHAR(size): 0-65535 ",
        "TINYTEXT: 0-255(2^8-1)",
        "TEXT(size): 65,535(2^16-1): 64KB",
        "MEDIUMTEXT: 16,777,215(2^24-1): 16MB",
        "LONGTEXT: 4,294,967,295(2^32-1): 4GB",
        "ENUM(val1, val2, val3,...): 65,535(2^16-1): 64KB",
        "SET( val1,val2,val3,....): 64(2^6)",
    ]



# _________________________________________________________________________________________________________________
# Get SQL str datatype
# T*
def get_int_datatype():
    return [
        "TINYINT: h:(-128, 127), n:(0, 255)",
        "SMALLINT: h:(-32 768, 32 767), n:(0, 65 535)",
        "MEDIUMINT: h:(-8 388 608, 8 388 607), n:(0, 16 777 215)",
        "INT: h:(-2 147 483 648, 2 147 483 647), n:(0, 4 294 967 295)",
        "INTEGER: h:(-2 147 483 648, 2 147 483 647), n:(0, 4 294 967 295)",
        "BIGINT: h:(-2^63, 2^63-1), n:(0, 2^64-1)",
    ]



# _________________________________________________________________________________________________________________
# Get SQL float datatype
# T*
def get_float_datatype():
    return [
        "FLOAT(size, d): 4 byte",
        "FLOAT(p): when p = 0-24, FLOAT(), when p = 25-53, DOUBLE(),  ",
        "DOUBLE(size, d): 8 byte",
        "DECIMAL(size, d): size: 0-65, default=10, d: 0-30, default=0)",
        "DEC(size, d): == DECIMAL(size, d)",
    ]



# _________________________________________________________________________________________________________________
# Get SQL date datatype
# T*
def get_date_datatype():
    return [
        "DATE: YYYY-MM-DD = from '1000-01-01' to '9999-12-31'",
        "DATETIME(fsp): YYYY-MM-DD hh:mm:ss = from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'",
        "TIMESTAMP(fsp): '1970-01-01 00:00:00' UTC to now: YYYY-MM-DD hh:mm:ss: '1970-01-01 00:00:01' UTC to now UTC",
        "TIME(fsp): hh:mm:ss = '-838:59:59' to '838:59:59'",
        "YEAR: 1901 to 2155, 0000",
    ]




# _________________________________________________________________________________________________________________
# Get SQL bit datatype
# T*
def get_bit_datatype():
    return [
        "BIT(size): 0-64, default=0",
        "BINARY(size): == CHAR(), default=1",
        "VARBINARY(size): == VARCHAR()",
        "TINYBLOB: 0-255 (2^8-1) byte",
        "BLOB(size): 0-65,535 (2^16-1) byte = 64KB",
        "MEDIUMBLOB: 0-16,777,215 (2^24-1) byte = 16MB",
        "LONGBLOB: 0-42,94,967,295 (2^32-1) byte = 4GB",
    ]




# _________________________________________________________________________________________________________________
# Get SQL MySQL Date Function
# T*
def get_MySQL_Date_Func():
    return [
        "NOW(): 2066-06-16 06:06:36",
        "CURDATE(): 2066-06-16",
        "CURTIME(): 06:06:36",
        "DATE(date): 2066-06-16",
        "EXTRACT(unit FROM date): unit in [get_MySQL_Date_Func_EXTRACT]",
        "DATE_ADD(date, INTERVAL expr type): in [get_MySQL_Date_Func_DATE_ADD]",
        "DATE_SUB(date, INTERVAL expr type): in [get_MySQL_Date_Func_DATE_SUB]",
        "DATEDIFF(date1,date2)",
        "DATE_FORMAT(date, format): format in [get_MySQL_Date_Func_DATE_FORMAT]",
        "CURTIME(): 06:06:36",
        "CURTIME(): 06:06:36",
    ]



# _________________________________________________________________________________________________________________
# Get SQL MySQL Func EXTRACT(unit FROM date)
# T*
def get_MySQL_Date_Func_EXTRACT():
    return [
        "MICROSECOND","SECOND","MINUTE","HOUR","DAY","WEEK","MONTH","QUARTER","YEAR","SECOND_MICROSECOND","MINUTE_MICROSECOND","MINUTE_SECOND","HOUR_MICROSECOND","HOUR_SECOND","HOUR_MINUTE","DAY_MICROSECOND","DAY_SECOND","DAY_MINUTE","DAY_HOUR","YEAR_MONTH"
    ]



# _________________________________________________________________________________________________________________
# Get SQL MySQL Func DATE_ADD(date, INTERVAL expr type)
# T*
def get_MySQL_Date_Func_DATE_ADD():
    return [
        "MICROSECOND","SECOND","MINUTE","HOUR","DAY","WEEK","MONTH","QUARTER","YEAR","SECOND_MICROSECOND","MINUTE_MICROSECOND","MINUTE_SECOND","HOUR_MICROSECOND","HOUR_SECOND","HOUR_MINUTE","DAY_MICROSECOND","DAY_SECOND","DAY_MINUTE","DAY_HOUR","YEAR_MONTH"
    ]



# _________________________________________________________________________________________________________________
# Get SQL MySQL Func DATE_SUB(date, INTERVAL expr type)
# T*
def get_MySQL_Date_Func_DATE_SUB():
    return [
        "MICROSECOND","SECOND","MINUTE","HOUR","DAY","WEEK","MONTH","QUARTER","YEAR","SECOND_MICROSECOND","MINUTE_MICROSECOND","MINUTE_SECOND","HOUR_MICROSECOND","HOUR_SECOND","HOUR_MINUTE","DAY_MICROSECOND","DAY_SECOND","DAY_MINUTE","DAY_HOUR","YEAR_MONTH"
    ]



# _________________________________________________________________________________________________________________
# Get SQL MySQL Func DATE_FORMAT(date, format) candidates
# T*
def get_MySQL_Date_Func_DATE_FORMAT():
    return [
        "%a abbreviated name of the week",
        "%b abbreviated month name",
        "%c month, value",
        "%D Days in a month with an English prefix",
        "%d day of the month, value (00-31)",
        "%e days of the month, value (0-31)",
        "%f microseconds",
        "%H hours (00-23)",
        "%h hours (01-12)",
        "%I hour (01-12)",
        "%i minutes, value (00-59)",
        "%j years of days (001-366)",
        "%k hours (0-23)",
        "%l hours (1-12)",
        "%M month name",
        "%m month, value (00-12)",
        "%p AM or PM",
        "%r time, 12-hours (hh:mm:ss AM or PM)",
        "%S seconds (00-59)",
        "%s seconds (00-59)",
        "%T time, 24-hours (hh:mm:ss)",
        "%U Sunday is the first day of the week",
        "%u Monday is the first day of the week",
        "%V Week (01-53) Sunday is the first day of the week, used with %X",
        "%v Monday is the first day of the week, used with %x",
        "%W week name",
        "%w week days (0= Sunday, 6= Saturday)",
        "%X years, where Sunday is the first day of the week, 4 bits, and %V are used",
        "%x years, where Monday is the first day of the week, 4 bits, used with %v",
        "%Y years, 4 places",
        "%y"
    ]



# _________________________________________________________________________________________________________________
# Get SQL Server Date
# T*
def get_SQL_Server_Date():
    return [
        "GETDATE(): 2066-06-16 06:06:36.666",
        "DATEPART(datepart, date): datepart in [get_SQL_Server_Date_DATEPART]",
        "DATEADD(datepart, number, date): date in [get_SQL_Server_Date_DATEADD]",
        "DATEDIFF(datepart, startdate, enddate): date in [get_SQL_Server_Date_DATEDIFF]"
        "CONVERT(data_type(length), data_to_be_converted, style): date in [get_SQL_Server_Date_CONVERT]"
    ]



# _________________________________________________________________________________________________________________
# Get SQL Server Date DATEPART
# T*
def get_SQL_Server_Date_DATEPART():
    return [
        "Year = yy, yyyy",
        "A quarter = a quarter",
        "Month = mm, m",
        "Day of the year = dy, y",
        "Day = dd, d",
        "Week = wk, a ww",
        "Week = dw, w",
        "Hour = hh",
        "Minutes = mi, n",
        "Second = ss, s",
        "Millisecond = ms",
        "Microsecond = MCS",
        "Nanosecond = ns"
    ]


# _________________________________________________________________________________________________________________
# Get SQL Server Date DATEADD
# T*
def get_SQL_Server_Date_DATEADD():
    return [
        "Year = yy, yyyy",
        "A quarter = a quarter",
        "Month = mm, m",
        "Day of the year = dy, y",
        "Day = dd, d",
        "Week = wk, a ww",
        "Week = dw, w",
        "Hour = hh",
        "Minutes = mi, n",
        "Second = ss, s",
        "Millisecond = ms",
        "Microsecond = MCS",
        "Nanosecond = ns"
    ]



# _________________________________________________________________________________________________________________
# Get SQL Server Date DATEDIFF
# T*
def get_SQL_Server_Date_DATEDIFF():
    return [
        "Year = yy, yyyy",
        "A quarter = a quarter",
        "Month = mm, m",
        "Day of the year = dy, y",
        "Day = dd, d",
        "Week = wk, a ww",
        "Week = dw, w",
        "Hour = hh",
        "Minutes = mi, n",
        "Second = ss, s",
        "Millisecond = ms",
        "Microsecond = MCS",
        "Nanosecond = ns"
    ]



# _________________________________________________________________________________________________________________
# Get SQL Server Date CONVERT
# T*
def get_SQL_Server_Date_CONVERT():
    return [
        "100 OR 0 = mon dd yyyy hh:miAM (or PM)",
        "101 = mm/dd/yy",
        "102 = yy.mm.dd",
        "103 = dd/mm/yy",
        "104 = dd.mm.yy",
        "105 = dd-mm-yy",
        "106 = dd mon yy",
        "107 = Mon dd, yy",
        "108 = hh:mm:ss",
        "109 or 9 = mon dd yyyy hh:mi:ss:mmmAM(or PM)",
        "110 = mm-dd-yy",
        "111 = yy/mm/dd",
        "112 = yymmdd",
        "113 or 13 = dd mon yyyy hh:mm:ss:mmm(24h)",
        "114 = hh:mi:ss:mmm(24h)",
        "120 or 20 = yyyy-mm-dd hh:mi:ss(24h)",
        "121 or 21 = yyyy-mm-dd hh:mi:ss.mmm(24h)",
        "126 = yyyy-mm-ddThh:mm:ss.mmm(not sapce)",
        "130 = dd mon yyyy hh:mi:ss:mmmAM",
        "131 = dd/mm/yy hh:mi:ss:mmmAM"
    ]

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
def no_quotes_tuple_str(tuple:tuple):
    """
    Delete the single quotes in a tuple str
    """
    return delete_quotes_in_str(str(tuple))



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
def sql_DROP_TABLE_IF_EXISTS_table(table):
    return "DROP TABLE IF EXISTS " + str(table) + ";"



# _________________________________________________________________________________________________________________
# Get SQL code: SHOW TABLES;
# T*
def sql_SHOW_TABLES(db):
    sql = "use " + str(db) + "; SHOW TABLES;"
    return sql 




# _________________________________________________________________________________________________________________
# Get SQL code: CREATE TABLE table(table_detail_list)
# T*
def sql_CREATE_TABLE_table_tDetail(db, table, table_detail):
    sql = ''
    str_table_detail = ''
    if isinstance(table_detail, str):
        str_table_detail = table_detail
    elif isinstance(table_detail, list):
        str_table_detail = str2DList_to_1str(table_detail)
        
    sql = "use " + str(db) + "; " + "CREATE TABLE " + str(table) + "(" + str_table_detail + ");"
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DROP TABLE table;
# T*
def sql_DROP_TABLE_table(db, table):
    sql = "use " + str(db) + "; " + "DROP TABLE " + str(table) + ";"
    return sql 



# ________________________________________________________________________________________________________________
# Get SQL code: DROP DATABASE db;
# T*
def sql_DROP_DATABASE_db(db):
    sql = "SHOW DATABASE " + str(db) + ";"
    # print(sql)
    return sql 



# ________________________________________________________________________________________________________________
# Get SQL code: TRUNCATE TABLE table;
# T*
def sql_TRUNCATE_TABLE_table(db, table):
    sql = "use " + str(db) + "; " + "TRUNCATE TABLE " + str(table) + ";"
    print(sql)
    return sql 


# ________________________________________________________________________________________________________________
# Get SQL code: DESCRIBE tableName;
# T*
def sql_DESCRIBE_table(db, table):
    sql = "use " + str(db) + "; " + "DESCRIBE " + str(table) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SHOW COLUMNS FROM tableName
# T*
def sql_SHOW_COLUMNS_FROM_table(db, table):
    sql = "SHOW COLUMNS FROM " + str(table) + " FROM " +  str(db) + ";"
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM tableName
# T*
def sql_SELECT_ALL_FROM_table(db, table):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + ";"
    return sql 



# _________________________________________________________________________________________________________________
def sql_INSERT_INTO_table_columnsTuple_VALUES_valuesTuple(db:str, table:str, colomums_tuple:tuple, values_tuple:tuple):
    """
    Get SQL code: INSERT INTO colomums_tuple tableName VALUES values_tuple
    """
    sql = "use " + str(db) + "; " + "INSERT INTO " + str(table) + " " + no_quotes_tuple_str(colomums_tuple) + " VALUES " + str(values_tuple) + ";"
    # print(f'{sql = }')
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tableName VALUES (...), (...), ...
# T*
def sql_INSERT_INTO_table_VALUES_tuple(db, table, tuple):
    tuple_str = str(tuple)
    sql = "use " + str(db) + "; " + "INSERT INTO " + str(table) + " VALUES " + tuple_str + ";"
    # print(f'{sql = }')
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tableName VALUES (...), (...), ...
# T*
def sql_INSERT_INTO_table_VALUES_multiTuples(db, table, tuples_list):
    values_str = str2DList_to_1d_tupleStr(tuples_list)
    sql = "use " + str(db) + "; " + "INSERT INTO " + str(table) + " VALUES " + values_str + ";"
    # print(f'{sql = }')
    return sql 
    


# _________________________________________________________________________________________________________________
# Get SQL code: INSERT INTO tablename (field,field2,...) VALUES (value, value2,...);
# T*
def sql_INSERT_INTO_table_filedTuple_VALUES_valueTuples(db, table, filed_list, tuple_list):
    fileds_str_t = tuple(filed_list)
    # values_str = str2DList_to_1d_tupleStr(tuple_list)
    values_str_t = tuple(tuple_list)
    sql = "use " + str(db) + "; " + "INSERT INTO " + str(table) + " " + delete_quotes_in_str(str(fileds_str_t)) + " VALUES " + str(values_str_t) + ";"
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
def sql_SELECT_column_FROM_table(db, column_list, table):
    column_list_str = ''
    for i in range(len(column_list)):
        if i < len(column_list)-1:
            column_list_str += column_list[i].strip() + ','
        else:
            column_list_str += column_list[i].strip()

    sql = "use " + str(db) + "; " + "SELECT " + str(column_list_str) + " FROM " + str(table) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT [column_list] FROM tableName
# T*
def sql_SELECT_columnList_FROM_table(db, column_list, table):
    return sql_SELECT_column_FROM_table(db, column_list, table) 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT DISTINCT column FROM tableName
# T*
def sql_SELECT_DISTINCT_column_FROM_table(db, column_list, table):
    column_list_str = ''
    for i in range(len(column_list)):
        if i < len(column_list)-1:
            column_list_str += column_list[i].strip() + ','
        else:
            column_list_str += column_list[i].strip()
    sql = "use " + str(db) + "; " + "SELECT DISTINCT " + str(column_list_str) + " FROM " + str(table) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT DISTINCT [column_list] FROM tableName
# T*
def sql_SELECT_DISTINCT_columnList_FROM_table(db, column_list, table):
    return sql_SELECT_DISTINCT_column_FROM_table(db, column_list, table) 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM tableName WHERE condition
# T*
def sql_SELECT_ALL_FROM_table_WHERE_condition(db, table, condition):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(condition) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ...
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList(db, column_list, table, order_lsit):
    sql = "use " + str(db) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_DESC(db, column_list, table, order_lsit):
    sql = "use " + str(db) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " DESC;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT fileds, ... FROM Orders ORDER BY orders, ..., DESC
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_ASC(db, column_list, table, order_lsit):
    sql = "use " + str(db) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " ASC;"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: ELECT fileds, ... FROM Orders ORDER BY orders, ..., condition
# T*
def sql_SELECT_columnList_FROM_table_ORDER_BY_conList_condition(db, column_list, table, order_lsit, condition):
    sql = "use " + str(db) + "; " + "SELECT " + delete_quotes_in_str(str(column_list))[1:-1] + " FROM " + str(table) + " ORDER BY " + delete_quotes_in_str(str(order_lsit))[1:-1] + " " + str(condition) + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: UPDATE table SET column_kv_list WHERE column_conkv_list
# T*
def sql_UPDATE_table_SET_columnKvlist_WHERE_columnConkvList(db, table, column_kv_list, column_conkv_list):
    sql = "use " + str(db) + "; " + "UPDATE " + str(table) + " SET " + kvList_2_kvStr(column_kv_list) + " WHERE " + kvList_2_kvStr(column_conkv_list) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DELETE FROM table WHERE k=v
# T*
def sql_DELETE_FROM_table_WHERE_kv(db, table, column_conkv):
    sql = "use " + str(db) + "; " + "DELETE FROM " + str(table) + " WHERE " + kvList_2_kvStr([column_conkv]) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: DELETE * FROM table 
# T*
def sql_DELETE_ALL_FROM_table_WHERE_kv(db, table):
    sql = "use " + str(db) + "; " + "DELETE * FROM " + str(table) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table LIMIT limit_num; 
# T*
def sql_SELECT_ALL_FROM_table_LIMIT_num(db, table, limit_num):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " LIMIT " + str(limit_num) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table LIMIT a,b; 
# T*
def sql_SELECT_ALL_FROM_table_LIMIT_a_to_b(db, table, a, b):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " LIMIT " + str(a-1) + "," + str(b-a+1) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str(x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE start with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_startWith_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str(x+'%') + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE end with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_endWith_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str('%'+x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE between x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_between_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str('%'+x+'%') + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE " + sql_str(x) + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE start with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_startWith_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE " + sql_str(x+'%') + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE end with x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_endWith_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE " + sql_str('%'+x) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE include x
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_include_x(db, table, column, x):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE " + sql_str('%'+x+'%') + ";"
    print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE condition
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_condition(db, table, column, condition):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str(condition) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE condition
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_condition(db, table, column, condition):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE " + sql_str(condition) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE startWithLetters
# T
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_startWithLetters(db, table, column, letters_list):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE " + sql_str("[" + combine_chars_to_aStr(letters_list) + "]%")  + ";"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE notstartWithLetters
# T
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_notStartWithLetters(db, table, column, letters_list):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE [!" + combine_chars_to_aStr(letters_list) + "]%;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column LIKE BINARY condition
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_BINARY_condition(db, table, column, condition):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " LIKE BINARY '" + combine_chars_to_aStr(condition) + "%';"
    print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM table WHERE column NOT LIKE BINARY condition
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_BINARY_condition(db, table, column, condition):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT LIKE BINARY '" + combine_chars_to_aStr(condition) + "%';"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column IN (tiems tuple)
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_IN_tuple(db, table, column, tuple):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " IN " + strTuple(tuple) + ";"
    # print(sql)
    return sql 




# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column IN (tiems tuple)
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_IN_tuple(db, table, column, tuple):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " NOT IN " + strTuple(tuple) + ";"
    # print(sql)
    return sql 




# _________________________________________________________________________________________________________________
# Get SQL code:  SELECT * FROM Persons WHERE column BETWEEN a AND b
# T*
def sql_SELECT_ALL_FROM_tabl_WHERE_column_BETWEEN_a_AND_b(db, table, column, a, b):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(table) + " WHERE " + str(column) + " BETWEEN " + sql_str(a) + " AND " + sql_str(b) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column AS c FROM table 
# T*
def sql_SELECT_column_AS_c_FROM_table(db, column, c, table):
    sql = "use " + str(db) + "; " + "SELECT " + str(column)  + " AS " + str(c) + " FROM " + str(table) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column FROM table AS t
# T*
def sql_SELECT_column_FROM_table_AS_t(db, column, table, t):
    sql = "use " + str(db) + "; " + "SELECT " + str(column)  + " FROM " + str(table) + " AS " + str(t) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT column AS c FROM table AS t
# T*
def sql_SELECT_column_AS_c_FROM_table_AS_t(db, column, c, table, t):
    sql = "use " + str(db) + "; " + "SELECT " + str(column)  + " AS " + str(c) +  " FROM " + str(table) + " AS " + str(t) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta [inner] JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_INNER_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " INNER JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta LEFT JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta FULL JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_FULL_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " FULL JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta FULL OUTER JOIN b on a.key = b.key
# T*
def sql_SELECT_ALL_FROM_ta_FULL_OUTER_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " FULL OUTER JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta LEFT JOIN b on a.key = b.key UNION SELECT * FROM ta RIGHT JOIN b on a.key = b.key UNION 
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + \
        " UNION " + "SELECT * FROM " + str(ta) + " RIGHT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta LEFT JOIN b on a.key = b.key WHERE b.key IS NULL
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_WHERE_bkey_IS_NULL(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + \
        " WHERE " + str(tb) + "." + str(key)  + " IS NULL;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta RIGHT JOIN b on a.key = b.key WHERE a.key IS NULL
# T*
def sql_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey_WHERE_akey_IS_NULL(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " RIGHT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + \
        " WHERE " + str(ta) + "." + str(key)  + " IS NULL;"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM a FULL OUTER JOIN a on a.key = a.key (not for mysql)
# T*
def sql_SELECT_ALL_FROM_ta_OUTER_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " OUTER JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";"
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: select * from A left join B on A.key = B.key union select * from A right join B on A.key = B.key (for mysql)
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) \
    + " UNION " +  "SELECT * FROM " + str(ta) + " RIGHT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + ";" 
    # print(sql)
    return sql 



# _________________________________________________________________________________________________________________
# Get SQL code: SELECT * FROM ta LEFT JOIN tb b ON ta.key=tb.key WHERE tb.key IS NULL UNION SELECT * FROM ta RIGHT JOIN tb b ON ta.key=tb.key WHERE a.key IS NULL；
# T*
def sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_sql_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey(db, ta, tb, key):
    sql_left =  sql = "use " + str(db) + "; " + "SELECT * FROM " + str(ta) + " LEFT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + \
        " WHERE " + str(tb) + "." + str(key)  + " IS NULL"
    sql_right = "SELECT * FROM " + str(ta) + " RIGHT JOIN " + str(tb) + " ON " + str(ta) + "." + str(key) + " = " + str(tb) + "." + str(key) + \
        " WHERE " + str(ta) + "." + str(key)  + " IS NULL;"
    sql = sql_left + " UNION " + sql_right
    # print(sql)
    return sql


# _________________________________________________________________________________________________________________
# Get SQL code: SELECT a INTO t_new FROM t_old
# T*
def sql_SELECT_a_INTO_tn_FROM_to(db, a, tn, to):
    sql = "use " + str(db) + "; " + "SELECT " + str(a) + " INTO " + str(tn) + " FROM " + str(to) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: CREATE DATABASE db
# T*
def sql_CREATE_DATABASE_db(db):
    sql = "CREATE DATABASE " + str(db) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: DROP INDEX index_name ON table (for Microsoft SQLJet and Microsoft Access)
# T*
def sql_DROP_INDEX_index_ON_table(index, table):
    sql = "DROP INDEX " + str(index) + " ON " + str(table) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: DROP INDEX table.index_name (for MS SQL Server)
# T*
def sql_DROP_INDEX_table_DOT_index(table, index):
    sql = "DROP INDEX " + str(table) + "." + str(index) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: DROP INDEX index_name (for IBM DB2 and Oracle)
# T*
def sql_DROP_INDEX_index(index):
    sql = "DROP INDEX " + str(index) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: ALTER TABLE table DROP INDEX index 
# T*
def sql_ALTER_TABLE_table_DROP_INDEX_index(db, table, index):
    sql = "use " + str(db) + "; " + "ALTER TABLE " + str(table) + " DROP INDEX " + str(index) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: ALTER TABLE table ADD column datetype
# T*
def sql_ALTER_TABLE_table_ADD_column_datatype(db, table, column, datatype):
    sql = "use " + str(db) + "; " + "ALTER TABLE " + str(table) + " ADD " + str(column) + " " + str(datatype) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: ALTER TABLE table DROP COLUMN column 
# T*
def sql_ALTER_TABLE_table_DROP_COLUMN_column(db, table, column):
    sql = "use " + str(db) + "; " + "ALTER TABLE " + str(table) + " DROP COLUMN " + str(column) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: ALTER TABLE table ALTER COLUMN column datatype
# T*
def sql_ALTER_TABLE_table_ALTER_COLUMN_column_datatype(db, table, column, datatype):
    sql = "use " + str(db) + "; " + "ALTER TABLE " + str(table) + " ALTER COLUMN " + str(column) + " " + str(datatype) + ";" 
    # print(sql)
    return sql




# _________________________________________________________________________________________________________________
# Get SQL code: ALTER TABLE table AUTO_INCREMENT=num
# T*
def sql_ALTER_TABLE_table_AUTO_INCREMENT_equal_num(db, table, num):
    sql = "use " + str(db) + "; " + "ALTER TABLE " + str(table) + " AUTO_INCREMENT=" + str(num) + ";" 
    # print(sql)
    return sql


# _________________________________________________________________________________________________________________
# Get SQL code: CREATE VIEW a AS b
# T*
def sql_CREATE_VIEW_a_AS_b(db, a, b):
    sql = "use " + str(db) + "; " + "CREATE VIEW " + str(a) + " AS " + str(b) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
# Get SQL code: DROP VIEW view
# T*
def sql_DROP_VIEW_view(db, view):
    sql = "use " + str(db) + "; " + "DROP VIEW " + str(view) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
def sql_SELECT_COUNT_column_FROM_table(db:str, column:str, table:str):
    """
    Get SQL code: SELECT COUNT(column_name) FROM table_name
    """
    sql = "use " + str(db) + "; " + "SELECT COUNT(" + str(column) + ")" + " FROM " + str(table) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
def sql_SELECT_COUNT_ALL_FROM_table(db:str, table:str):
    """
    Get SQL code: SELECT COUNT(*) FROM table_name
    """
    sql = "use " + str(db) + "; " + "SELECT COUNT(*)" + " FROM " + str(table) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
def sql_SELECT_COUNT_DISTINCT_column_FROM_table(db:str, column:str, table:str):
    """
    Get SQL code: SELECT COUNT(DISTINCT column_name) FROM table_name
    """
    sql = "use " + str(db) + "; " + "SELECT COUNT(DISTINCT " + str(column) + ")" + " FROM " + str(table) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
def sql_SELECT_COUNT_condition_FROM_table(db:str, con:str, table:str):
    """
    Get SQL code: SELECT COUNT condition FROM table
    """
    sql = "use " + str(db) + "; " + "SELECT COUNT " + str(con) + " FROM " + str(table) + ";" 
    # print(sql)
    return sql



# _________________________________________________________________________________________________________________
def sql_SELECT_COUNT_condition1_FROM_table_WHERE_condition2(db:str, con1:str, table:str, con2:str):
    """
    Get SQL code: SELECT COUNT condition1 FROM table WHERE condition2
    """
    sql = "use " + str(db) + "; " + "SELECT COUNT " + str(con1) + " FROM " + str(table) + " WHERE " + str(con2) + ";" 
    # print(sql)
    return sql

