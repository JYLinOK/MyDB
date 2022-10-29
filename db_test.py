import mariadb
import mydb



user_m = "root"
password_m = "123123"
host_m = "192.168.1.2"
port_m = 3306
database_m = ""


conn = mariadb.connect(user=user_m, password=password_m, host=host_m, port=port_m, database=database_m)

cur = conn.cursor()

# print(f'{mydb.get_version(cur) = }')

# sql = 'use db1; CREATE TABLE db1_tb1(name varchar(20) not null, id int,gender char(1));'
# mydb.SQL(cur, sql)

# print(f'{mydb.split_str_by_spList_ret_list(sql) = }')

a = [
    "name varchar(20) not null",
    "id int",
    "id2 int",
    "id3 int",
    "gender char(1)"
]
print(f'{mydb.SQL(cur, mydb.sql_CREATE_TABLE_use_dbName_create_tableName("db1", "t1", a)) = }')



cur.close()
conn.close()
