from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
import os
import mariadb
app = Flask(__name__)
app.secret_key = os.urandom(24)  # 用于管理session

# 数据库配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '240700'
app.config['MYSQL_DB'] = 'test1'

mysql = MySQL(app)

mariadb.pre_exec()
mariadb.tables()
mariadb.add_demo_data()
@app.route('/login', methods=['POST'])
def login():
    # 获取请求中的用户名和密码
    username = request.json.get('username')
    password = request.json.get('password')

    # 连接数据库验证用户
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        # 登录成功，保存用户信息到session
        session['user_id'] = user[0]
        session['username'] = user[1]
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


# 展示当前登录用户信息接口
@app.route('/', methods=['GET'])
def get_user_info():
    # 检查用户是否已登录
    if 'user_id' not in session:
        return jsonify({"message": "User not logged in"}), 403

    # 获取当前用户的详细信息
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT username, student_id, name, age FROM users WHERE id = %s", (session['user_id'],))
    user_info = cursor.fetchone()

    if user_info:
        user_data = {
            "username": user_info[0],
            "student_id": user_info[1],
            "name": user_info[2],
            "age": user_info[3]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"message": "User not found"}), 404


# 登出接口
@app.route('/logout', methods=['POST'])
def logout():
    # 清除session
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == '__main__':

    app.run(debug=True)

