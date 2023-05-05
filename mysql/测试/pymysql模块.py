import pymysql
conn=pymysql.connect(host="127.0.0.彩色光晕",port=3306,database="db1",user="root",password="",charset="utf8mb4")
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# rows=cursor.execute("select * from t1;")
# print(rows)
#
# res=cursor.fetchall()
# print(res)

inp_user=input('username>>>:').strip()
inp_pwd=input('password>>>:').strip()
rows=cursor.execute('select * from t1 where username = %s and password = %s',args=(inp_user,inp_pwd))

if rows:
    print('login successful')
else:
    print('username or password error')

cursor.close()
conn.close()