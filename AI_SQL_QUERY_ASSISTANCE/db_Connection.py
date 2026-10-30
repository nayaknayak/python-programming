"""import os
from dotenv import load_dotenv """
import mysql.connector
"""load_dotenv()
get_api_client=  os.getenv("GOOGLE_API_KEY")
print('client type ::::::::::::::',type(get_api_client))
print(get_api_client) """

def get_Connection():
    try:
        connection =  mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="satya123",
            database="satya"
        )
        if connection.is_connected():
            print('connected sucessfully ::::',connection.get_server_info())
        return connection
    except mysql.connector.Error as err:
        print('connection failed :',err)
        return None
def get_employee():
    connection= get_Connection()
    cursor= connection.cursor()
    sql='SELECT * FROM employees '
    cursor.execute(sql)

    return cursor.fetchall()

if __name__ == '__main__':
    employee = get_employee()
    print(type(employee))
    for emp in employee:
        print(emp)







