import mysql.connector

def remove_info(connection, data):
    cursor = connection.cursor()
    query="""
    delete from info where 姓名=%s
    """
    cursor.execute(query, (data,))
    connection.commit()
    print("Successfully removed data")


db_config = {'host': 'localhost', 'user': 'root', 'password': '240700', 'database': 'stu'}

connection = mysql.connector.connect(**db_config)

if connection.is_connected():
    db_info=connection.get_server_info()
    print(f"Connected to {db_info}")

   # new_student="安度因"
   # new_student="faker"
   # new_student="GULDAN"
    new_student="伊利丹"
    #new_student="李四"
    remove_info(connection, new_student)
    connection.close()
    print("Connection closed")
