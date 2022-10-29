import mariadb




user_m = "root"
password_m = "123123"
host_m = "192.168.1.2"
port_m = 3306
database_m = ""


conn = mariadb.connect(user=user_m, password=password_m, host=host_m, port=port_m, database=database_m)

cur = conn.cursor()


sql = "use db1;"
cur.execute(sql)

# sql = '''CREATE TABLE tbl(
#    product_id INT NOT NULL AUTO_INCREMENT,
#    product_name VARCHAR(100) NOT NULL,
#    product_manufacturer VARCHAR(40) NOT NULL,
#    submission_date DATE,
#    PRIMARY KEY ( product_id )
# );
# '''

# cur.execute(sql)


sql = "SHOW DATABASES;"
cur.execute(sql)





result = cur.fetchall()


print(f'{result = }')


# for one in result:
#     print(one)

cur.close()
conn.close()
