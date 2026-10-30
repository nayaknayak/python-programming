from mysql.connector import Error

from db_Connection import get_Connection


def execute_sql(sql):
    try:
        connection = get_Connection()
        cursor = connection.cursor()
        if not sql.strip().upper().startswith("SELECT"):
            raise ValueError("Only Seelct Query Accepted")
        cursor.execute(sql)
        return cursor.fetchall()
    except (Error,ValueError) as e:
        print("Error",e)

    finally:
        connection.close()
if __name__ == "__main__":
    result=execute_sql("SELECT * FROM employees")
    for row in result:
        print(row)
