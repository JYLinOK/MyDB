import mariadb
import mydb



user_m = "root"
password_m = "123123"
host_m = "192.168.1.2"
port_m = 3306
database_m = ""


# conn = mariadb.connect(user=user_m, password=password_m, host=host_m, port=port_m, database=database_m)


d = {
    "user":"root",
    "password": "123123",
    "host": "localhost",
    "port": 3306,
    "database": "",
}

conn, cur = mydb.connect_db_d(d)

# print(f'{mydb.get_version(cur) = }')

a = [
    "id int not null",
    "name char(10)"
]


print(f'{mydb.SQL(cur, mydb.sql_SELECT_ALL_FROM_table("db1", "t1")) = }')


# print(f'{mydb.SQL(cur, mydb.sql_SHOW_TABLES("db1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_CREATE_TABLE_use_db_create_table("db1", "t1", a)) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DROP_TABLE("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SHOW_COLUMNS_FROM_table("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DESCRIBE_tableName("db1", "t1")) = }')

# t = [[1, "this 1"], [2, "ok 123"], [3, "NO.3"], [4, "ok 123"]]
# print(f'{mydb.SQL(cur, mydb.sql_INSERT_INTO_table_VALUES_tuples("db1", "t1", t)) = }')

# print(f'{mydb.SQLcommit(cur,conn, mydb.sql_INSERT_INTO_table_filedTuple_VALUES_valueTuples("db1", "t1", ["id", "name"], [66, "is 66"])) = }')

# print(f'{mydb.SQL(cur, mydb.sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password("usr1", "localhost", "666")) = }')


# print(f'{mydb.SQL(cur, mydb.sql_SELECT_column_FROM_table("db1", "name", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SELECT_columnList_FROM_table("db1", ["id", "name"], "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SELECT_DISTINCT_column_FROM_table("db1", ["id", "name"], "t1")) = }')

# sql = mydb.sql_SELECT_ALL_FROM_table_WHERE_condiction("db1", "t1", "name='ok 123'")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_columnList_FROM_table_ORDER_BY_conList("db1", ["id"], "t1", ["name"])
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_columnList_FROM_table_ORDER_BY_conList_DESC("db1", ["id"], "t1", ["name"])
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.kvList_2_kvStr([['a', '123'], ['b', 789]])
# print(sql)

# sql = mydb.sql_SELECT_columnList_FROM_table_ORDER_BY_conList_condiction("db1", ["id"], "t1", ["name"], 'ASC')
# print(f"{mydb.SQL(cur, sql) = }")


# sql = mydb.sql_UPDATE_table_SET_columnKvlist_WHERE_columnConkvList("db1", "t1", [["id", 1]], [["name", "this 1"]])
# print(f"{mydb.SQLcommit(cur, conn, sql) = }")

# sql = mydb.sql_DELETE_FROM_table_WHERE_kv("db1", "t1", ["id", 1])
# print(f"{mydb.SQLcommit(cur, conn, sql) = }")

# sql = mydb.sql_DELETE_FROM_table_WHERE_kv("db1", "t1", ["id", 2])
# print(f"{mydb.SQLcommit(cur, conn, sql) = }")


sql = mydb.sql_SELECT_ALL_FROM_table_LIMIT_num("db1", "t1", 3)
print(f"{mydb.SQL(cur, sql) = }")












# conn.commit()
cur.close()
conn.close()
