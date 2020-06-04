import os
import datetime
import pymysql

username = os.getenv('C9_User')

connection = pymysql.connect(host='localhost',user = username, password='', db='Chinook')

try:
    # run q query and return a Dictionary
    with connection.cursor() as cursor:
        cursor.execute("""Create Table if not exists
                        FRIENDS(name char(20), age int, DOB datetime);""")
finally:
    connection.close()

