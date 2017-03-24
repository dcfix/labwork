import os
import cx_Oracle

connString = os.environ['DB_CIS']

sql = "select bi_lname, bi_fname from bi_personal_view_1 where bi_cust_nbr = 185107"

conn = cx_Oracle.connect(connString)

cur = conn.cursor()
cur.execute(sql)

for row in cur:
    print (row)
cur.close()

