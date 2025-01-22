import pymysql
def pre_exec():
    con=pymysql.connect(host='localhost',user='root',passwd='240700')
    print(con)
    cur=con.cursor()

    cur.execute('''CREATE DATABASE IF NOT EXISTS test1''')

    con.commit()
    con.close()

    tables()
    add_demo_data()

def tables():
    con=pymysql.connect(host='localhost',user='root',passwd='240700',database='test1')
    cur=con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,student_id INT NOT NULL, name VARCHAR(255) NOT NULL,age INT NOT NULL)''')
    con.commit()
    con.close()



def add_demo_data():
    con=pymysql.connect(host='localhost',user='root',passwd='240700',database='test1')
    cur=con.cursor()

    cur.execute('''INSERT INTO users (username,password,student_id,name,age)  SELECT "ruabeetu","240700",114514,"蔡徐坤",1000
    WHERE NOT EXISTS (
        SELECT 1 FROM users WHERE username = "ruabeetu" AND student_id = 114514)''')
    con.commit()
    con.close()



if __name__ == '__main__':
    pre_exec()

