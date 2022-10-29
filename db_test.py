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
    "name varchar(20) not null",
    "id int",
    "id2 int",
    "id3 int",
    "gender char(1)"
]


print(f'{mydb.SQL(cur, mydb.sql_SHOW_TABLES("db1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_CREATE_TABLE_use_dbName_create_tableName("db1", "t1", a)) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DROP_TABLE_tableName("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SHOW_COLUMNS_FROM_tableName("db1", "tbl")) = }')


cur.close()
conn.close()

# SHOW COLUMNS FROM tbl;
# SHOW COLUMNS FROM tb1;