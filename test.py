import mariadb
import mydb



user_m = "root"
password_m = "123123"
host_m = "192.168.1.2"
port_m = 3306
database_m = ""


conn = mariadb.connect(user=user_m, password=password_m, host=host_m, port=port_m, database=database_m)

cur = conn.cursor()

print(f'{mydb.get_version(cur) = }')









cur.close()
conn.close()
