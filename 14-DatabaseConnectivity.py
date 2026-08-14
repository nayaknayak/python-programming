# import sqlite3
# connection=sqlite3.connect("student_data.db")
# c=connection.cursor()

# cursor.execute("""
#     create table if not exists students_data(
#         student_id integer primary key autoincrement,
#         student_name text,
#         student_email text unique,
#         student_course text,
#         student_fee real
#     )
# """)
# print ("Student table created")
# sql = 'insert into students_data values(null,?,?,?,?)'


# name = input("Enter  name ?")
# email=input(" Enter Enail ?")
# course=input("Enter course ? ")
# fee=int(input(" Enter fee ?"))

# c.execute(sql,(name,email,course,fee))
# c.commit
# sqlShowTableData= "select * from students_data"
# res=c.execute(sqlShowTableData)
# fullrecords = res.fetchall()
# print(type(fullrecords))
# for record in fullrecords:
#     print(record)

# connection.commit()
# connection.close()


import mysql.connector
def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="satya123",
            database= "satya"
            )
        return connection
    except mysql.connector.Error as error:
        print(" connection failed :" , error)
        
def create_table(connection):
   # connection=get_connection()
    if connection is None:
       return  None
    try:
       cursor=connection.cursor();
       sql= """
              CREATE TABLE IF NOT EXISTS students (
              student_id INT PRIMARY KEY AUTO_INCREMENT,
              student_name VARCHAR(100) NOT NULL,
              student_email VARCHAR(100) UNIQUE NOT NULL,
              student_course VARCHAR(100) NOT NULL,
              student_fee DECIMAL(10, 2) NOT NULL
           )
           """
       cursor.execute(sql)
    except Exception as error:
        print(error)
print("1.Add a new Student ...")
print("2.View All Student...")
print("3.View Student by id:")
print("4.update student by id....")
print("5.Delete a Student")
print("6.Exit the application...")
choice =  int(input(" Please enter your operation : "))      
match choice:
    case 1: 
        try:
         connection=get_connection()
         create_table(connection)
         cursor=connection.cursor()
         sql= """
            INSERT INTO STUDENTS (STUDENT_NAME,STUDENT_EMAIL,STUDENT_COURSE,STUDENT_FEE)
            VALUES (%s,%s,%s,%s)
            """
         student_name= input("Enter Student Name : ")
         student_email= input("Enter Student email : ")
         student_course= input("Enter student course : ")
         student_fee= float(input("Enter Student fee : "))
         cursor.execute(sql,(student_name,student_email,student_course,student_fee))
         connection.commit()
        except Exception as exr:
            print("We got some error as : ",exr)
    case 2:
        try:
         connection=get_connection()
         create_table(connection)
         cursor=connection.cursor()
         sql= """
           SELECT * FROM STUDENTS
           """
         cursor.execute(sql)
         allRecords= cursor.fetchall()
         #print(allRecords,type(allRecords))
         for record in allRecords:
            print(record)
        except Exception as exp:
            print("No Data Found" , exp)
    case 3:
        try:
            connection=get_connection()
            cursor=connection.cursor()
            student_id= int(input("Enter your id to show Details?"))
            sql="""
            SELECT * FROM STUDENTS WHERE STUDENT_ID = (%s)
            """
            cursor.execute(sql,(student_id,))
            records= cursor.fetchone()
            print(records)
        except Exception as exp:
            print("Record not present as given id ",exp)
    case 4:
        try:
            connection=get_connection()
            cursor=connection.cursor()
            sql = """
            UPDATE STUDENTS SET STUDENT_NAME=%s, STUDENT_EMAIL=%s ,
            student_course=%s, student_fee =%s WHERE STUDENT_ID =%s
            """
            student_id=int(input("Enter your id to change the details :"))
            student_name= input("Enter your updated name?")
            student_email= input("Enter your updated email?")
            student_course= input("Enter your updated course?")
            student_fee=float(input("Enter your fee :"))
            cursor.execute(sql,(student_name,student_email,student_course,student_fee,student_id))
            connection.commit();
        except Exception as ex:
            print(ex)
    case 5:
      try:
        connection=get_connection()
        cursor=connection.cursor()
        sql = """
       delete from students where STUDENT_ID = (%s)
        """
        student_id=int(input("Enter your id Delete the records :"))
        cursor.execute(sql,(student_id,))
        connection.commit()
      except Exception as e:
         print(e)
    case 6:
        exit
    




























































