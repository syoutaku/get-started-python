import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='bluemix-sandbox-dal-9-portal.3.dblayer.com',
                                       database='compose',
                                       user='admin',
                                       password='LCRYBOGXDVKDLMWQ',
                                       port=29500)
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
            print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    connect()
