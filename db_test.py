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
    "host": "192.168.1.2",
    "port": 3306,
    "database": "",
}

conn, cur = mydb.connect_db_d(d)

# print(f'{mydb.get_version(cur) = }')

a = [
    "id int not null",
    "name char(10)"
]


# print(f'{mydb.SQL(cur, mydb.sql_SHOW_TABLES("db1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_CREATE_TABLE_use_db_create_table("db1", "t1", a)) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DROP_TABLE("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SHOW_COLUMNS_FROM_table("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DESCRIBE_tableName("db1", "t1")) = }')


# t = [[1, "this 1"], [2, "ok 123"], [3, "NO.3"]]
# print(f'{mydb.SQL(cur, mydb.sql_INSERT_INTO_table_VALUES_tuples("db1", "t1", t)) = }')


print(f'{mydb.SQL(cur, mydb.sql_CREATE_USER_username_AT_ip_IDENTIFIED_BY_password("usr1", "localhost", "666")) = }')


cur.close()
conn.close()

# SHOW COLUMNS FROM tbl;
# SHOW COLUMNS FROM tb1;