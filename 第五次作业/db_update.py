import mysql.connector

def update_info(connection, data):
    cursor = connection.cursor()
    query="""
    UPDATE info
    set 性别 = '未知'
    where 姓名=%s
    """
    cursor.execute(query, (data,))
    connection.commit()
    print("Successfully updated data")


db_config = {'host': 'localhost', 'user': 'root', 'password': '240700', 'database': 'stu'}

connection = mysql.connector.connect(**db_config)

if connection.is_connected():
    db_info=connection.get_server_info()
    print(f"Connected to {db_info}")


    update_info(connection,"RuabeeTu")
    connection.close()
    print("Connection closed")
