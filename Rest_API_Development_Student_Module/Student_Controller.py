# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:45:56 2026

@author: Admin
"""
from fastapi import FastAPI,HTTPException
import mysql.connector
from pydantic import BaseModel
from datetime import date
app=FastAPI()

class Student_Data_Management(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: int | None = None
    gender: str | None = None
    date_of_birth: date | None = None
    address: str | None = None
    department: str | None = None
    course: str | None = None
    admission_date: date | None = None
    student_status: str | None = None

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="satya123",
            database= "satya"
            )
       # print(dir(fastapi))
        return connection
    except Exception() as error:
        raise HTTPException (status_code= 500,detail="connection not established"+ str(error))

@app.on_event("startup")
def table_Creation():
    connection =  get_connection()
    if connection is None :
        return None
    else:
        try:
            cursour= connection.cursor()
            sql="""
                   CREATE TABLE IF NOT EXISTS student_maintable (
                   student_id VARCHAR(10) NOT NULL PRIMARY KEY,
                   first_name VARCHAR(50) NOT NULL,
                   last_name VARCHAR(50) NOT NULL,
                   email VARCHAR(100) NOT NULL UNIQUE,
                   phone VARCHAR(15),
                   gender VARCHAR(10),
                   date_of_birth DATE,
                   address VARCHAR(255),
                   department VARCHAR(100),
                   course VARCHAR(100),
                   admission_date DATE,
                   student_status VARCHAR(20) DEFAULT 'ACTIVE',
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                  ); 
                """
            cursour.execute(sql)
            connection.commit()
        except Exception as error:
            print(error)
@app.get("/all")          
def get_all_student():
    connection =  get_connection()
    cursor= connection.cursor()
    sql="""
    select * from student_maintable where student_status = 'ACTIVE'
    """
    try:
        cursor.execute(sql)
        obj= cursor.fetchall()
        if not obj :
            raise HTTPException(status_code=404, detail="NO Data Found")
        else:
            return{
                "status":[row for row in obj]
                }
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))
@app.get("/getbyid/{id}")
def get_student_by_id(id : str):
    connection =  get_connection()
    cursor= connection.cursor()
    sql="""
    select * from student_maintable where student_id = (%s) 
    and student_status = 'ACTIVE'
    """
    try:
        cursor.execute(sql,(id,))
        obj= cursor.fetchone()
        if not obj :
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            return {
                "status":obj
                }
    except Exception as error:
       raise HTTPException (status_code = 505, detail= str(error))
@app.post("/insert",status_code=200)
def data_input(student:Student_Data_Management):
    connection =  get_connection()
    cursor= connection.cursor()
    sql = """
     INSERT INTO student_maintable
     (
        student_id,
        first_name,
        last_name,
        email,
        phone,
        gender,
        date_of_birth,
        address,
        department,
        course,
        admission_date
     )
     VALUES
     (
        %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s
     )
     """
    sqlforgettingid= """
        select * from student_maintable order by student_id desc limit 1
    """
    try:
        cursor.execute(sqlforgettingid)
        obj= cursor.fetchone()
        if  obj:
            previous_student_id =  obj[0]
            previous_setudent_id_num=  (int(previous_student_id[3:])+1)
            if previous_setudent_id_num<10 :
                student_id= "std00"+str(previous_setudent_id_num)
            elif previous_setudent_id_num<100 :
                student_id= "std0"+str(previous_setudent_id_num)
            elif previous_setudent_id_num<1000 :
                student_id= "std"+str(previous_setudent_id_num)
        else:
            student_id ="std001"
        cursor.execute(sql,(student_id,student.first_name,student.last_name,
                            student.email,student.phone,student.gender,
                            student.date_of_birth,student.address,
                            student.department,student.course,
                            student.admission_date)) 
        connection.commit()
        return {
            "status":"sucessfully insert"
            }
    except Exception as error:
        raise HTTPException (ststus_code = 506, detail= str(error))
@app.put("/updateall/{id}")
def update_record(student:Student_Data_Management,id:str):
    connection =  get_connection()
    if connection is None :
        return None
    else:
        try:
            sql= """
            UPDATE student_maintable
                SET
                first_name = %s,
                last_name = %s,
                email = %s,
                phone = %s,
                gender = %s,
                    date_of_birth = %s,
                    address = %s,
                    department = %s,
                    course = %s,
                    admission_date = %s,
                    student_status = %s,
                    updated_at = CURRENT_TIMESTAMP
                    WHERE student_id = %s;
            """
            cursor=  connection.cursor()
            cursor.execute(sql,(student.first_name,student.last_name,
                                student.email,student.phone,student.gender,
                                student.date_of_birth,student.address,
                                student.department,student.course,
                                student.admission_date,student.student_status
                                ,id))
            connection.commit()
        except Exception as error:
            raise HTTPException (status_code = 506, detail= str(error))
@app.patch("/partialUpdate/{id}")
def update_partially(student: Student_Data_Management, id: str):

    connection = get_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed"
        )

    try:
        cursor = connection.cursor()

        # Check whether student exists
        sql_check = """
            SELECT student_id
            FROM student_maintable
            WHERE student_id = %s
        """

        cursor.execute(sql_check, (id,))
        obj = cursor.fetchone()

        if obj is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        # Get only the fields sent in PATCH request
        data = student.model_dump(exclude_unset=True)

        if not data:
            raise HTTPException(
                status_code=400,
                detail="No data provided for update"
            )

        # Allowed columns
        allowed_fields = {
            "first_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "date_of_birth",
            "address",
            "department",
            "course",
            "admission_date",
            "student_status"
        }
        #main logic
        set_values = []
        values = []

        for field, value in data.items():

            if field in allowed_fields:
                set_values.append(f"{field} = %s")
                values.append(value)

        # Build UPDATE query
        sql = f"""
            UPDATE student_maintable
            SET {", ".join(set_values)},
                updated_at = CURRENT_TIMESTAMP
            WHERE student_id = %s
        """
        
        values.append(id)

        cursor.execute(sql, tuple(values))

        connection.commit()

        return {
            "status": "success",
            "message": "Student updated successfully",
            "student_id": id,
            "updated_fields": list(data.keys())
        }

    except HTTPException:
        raise

    except Exception as error:
        connection.rollback()
        print(error)

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    finally:
        cursor.close()
        connection.close()
@app.delete("/delete/{id}",status_code=200)
def delete (id :str):
    try:
        connection=get_connection()
        if connection is None :
            raise HTTPException(
            status_code=500,
            detail="Database connection failed"
            )
        else:
            cursor= connection.cursor()
            sql= """
            update  student_maintable set student_status =  'INACTIVE' where 
                student_id =  (%s)
                
            """
            cursor.execute(sql,(id,))
            connection.commit()
            return{
                "ststus":"deleted sucessfully"
                }
    except Exception as error:
        raise HTTPException(ststus_code= 500, detail=str(error))
            
    
            
    

        
        
    
    
    
            
    
    
    