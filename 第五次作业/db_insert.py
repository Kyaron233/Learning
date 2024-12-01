import mysql.connector

def insert_info(connection, data):
    cursor = connection.cursor()
    query="""
    INSERT INTO info
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, data)
    connection.commit()
    print("Successfully inserted data")


db_config = {'host': 'localhost', 'user': 'root', 'password': '240700', 'database': 'stu'}

connection = mysql.connector.connect(**db_config)

if connection.is_connected():
    db_info=connection.get_server_info()
    print(f"Connected to {db_info}")

   # new_student=("安度因","男",20)
    #new_student=("GULDAN","male",200)
    new_student=("伊利丹","男",5000)
  #  new_student=("李四","女",17)
  #  new_student=("Faker","男",25)
    insert_info(connection, new_student)
    connection.close()
    print("Connection closed")
