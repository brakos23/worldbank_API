import pymysql
from flask import Flask, jsonify

conn = pymysql.connect(user='id',
                       password='Root123*',
                       database='worldbank',
                       host='db-world-bank.mysql.database.azure.com',
                       ssl={'ca': 'DigiCertGlobalRootCA.crt.pem'})

app = Flask(__name__)

@app.route('/topic', methods=['GET'])
def get_topic():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM topic"
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

