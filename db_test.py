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

# print(f'{mydb.SQL(cur, mydb.sql_CREATE_TABLE_table_tDetail("db1", "t1", a)) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DROP_TABLE("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_SHOW_COLUMNS_FROM_table("db1", "t1")) = }')

# print(f'{mydb.SQL(cur, mydb.sql_DESCRIBE_tableName("db1", "t1")) = }')

# t = [[1, "this 1"], [2, "ok 123"], [3, "NO.3"], [4, "ok 123"]]
# print(f'{mydb.SQL(cur, mydb.sql_INSERT_INTO_table_VALUES_tuples("db1", "t1", t)) = }')

# print(f'{mydb.SQLcommit(cur, conn, mydb.sql_INSERT_INTO_table_filedTuple_VALUES_valueTuples("db1", "t1", ["id", "name"], [66, "is 66"])) = }')

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

# sql = mydb.sql_SELECT_ALL_FROM_table_LIMIT_num("db1", "t1", 3)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_table_LIMIT_a_to_b("db1", "t1", 1, 5)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_x("db1", "t1", "name", "is 66")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_endWith_x("db1", "t1", "name", "66")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_between_x("db1", "t1", "name", "1")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_x("db1", "t1", "name", "NO.3")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_startWith_x("db1", "t1", "name", "N")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_endWith_x("db1", "t1", "name", "3")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_between_x("db1", "t1", "name", "6")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_condiction("db1", "t1", "name", "___123")
# print(f"{mydb.SQL(cur, sql) = }")

# print(f"{mydb.combine_chars_to_aStr(['c', 'h', 'i']) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_startWithLetters("db1", "t1", "name", ['o'])
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_LIKE_BINARY_condiction("db1", "t1", "name", 'ok')
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_LIKE_BINARY_condiction("db1", "t1", "name", 'ok')
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_IN_tuple("db1", "t1", "name", ("is 66"))
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_IN_tuple("db1", "t1", "name", ("is 66"))
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_NOT_IN_tuple("db1", "t1", "name", ("is 66"))
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_tabl_WHERE_column_BETWEEN_a_AND_b("db1", "t1", "id", 2, 3)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_column_AS_c_FROM_table("db1", "id", "i", "t1")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_column_FROM_table_AS_t("db1", "id", "t1", "t")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_column_AS_c_FROM_table_AS_t("db1", "id", "i",  "t1", "t")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_INNER_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_FULL_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_FULL_OUTER_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_WHERE_bkey_IS_NULL("db1", "t1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey_WHERE_akey_IS_NULL("db1", "ta", "tb", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_OUTER_JOIN_tb_ON_taKey_equal_tbKey("db1", "ta", "tb", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey("db1", "ta", "tb", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_ALL_FROM_ta_LEFT_JOIN_tb_ON_taKey_equal_tbKey_UNION_sql_SELECT_ALL_FROM_ta_RIGHT_JOIN_tb_ON_taKey_equal_tbKey("db1", "ta", "tb", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_a_INTO_tn_FROM_to("db1", "id", "ta", "tb")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_SELECT_a_INTO_tn_FROM_to_WHERE_con("db1", "id", "ta", "tb", "a=b")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_CREATE_DATABASE_db_name("db2")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_DROP_INDEX_index_ON_table("db1", 1, "t1")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_DROP_INDEX_table_DOT_index("t1", 1)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_DROP_INDEX_index(1)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_ALTER_TABLE_table_DROP_INDEX_index("db1", "t1", 1)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_DROP_DATABASE_db("db2")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_TRUNCATE_TABLE_table("db1", "tb1")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_ALTER_TABLE_table_ADD_column_datatype("db1", "tb1", "id", "TEXT")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_ALTER_TABLE_table_DROP_COLUMN_column("db1", "tb1", "id")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_ALTER_TABLE_table_ALTER_COLUMN_column_datatype("db1", "tb1", "id", "date")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_ALTER_TABLE_table_AUTO_INCREMENT_equal_num("db1", "tb1", 1)
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_CREATE_VIEW_a_AS_b("db1", "[a]", "b")
# print(f"{mydb.SQL(cur, sql) = }")

# sql = mydb.sql_CREATE_VIEW_a_AS_b("db1", "[a]")
# print(f"{mydb.(cur, sql) = }")

# sql = mydb.sql_INSERT_INTO_table_columnsTuple_VALUES_valuesTuple("db1", "t1", ('c1', 'c2', 'c3'), ('v1', 'v2', 'v3'))
# print(f"{mydb.SQLcommit(cur, conn, sql) = }")

# sql = mydb.sql_SELECT_COUNT_column_FROM_table("db1", "c1", "t1")
# print(f"{mydb.SQL(cur, conn, sql) = }")

# sql = mydb.sql_SELECT_COUNT_ALL_FROM_table("db1", "t1")
# print(f"{mydb.SQL(cur, conn, sql) = }")

# sql = mydb.sql_SELECT_COUNT_DISTINCT_column_FROM_table("db1", "c1", "t1")
# print(f"{mydb.SQL(cur, sql) = }")

sql = mydb.sql_SELECT_COUNT_condition1_FROM_table_WHERE_condition2("db1", "con1", "t1", "con2")
print(f"{mydb.SQL(cur, sql) = }")




# conn.commit()
cur.close()
conn.close()
