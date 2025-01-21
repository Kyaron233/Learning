import mariadb
conn = mariadb.connect(user="root",password="240700",database="test1",host="localhost")

cursor = conn.cursor()
#add="INSERT INTO users (id,username,password,student_id,name,age) VALUES (0,'admin','admin',1,'admin',1)"
add="INSERT INTO users (id,username,password,student_id,name,age) VALUES (114514,'ruabeetu','240700',2,'鲁阿北图',1000)"
cursor.execute(add)

conn.commit()
cursor.close()
conn.close()