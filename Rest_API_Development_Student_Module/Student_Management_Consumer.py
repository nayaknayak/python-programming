# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:53:35 2026

@author: Admin
"""
import requests
import streamlit as st

st.title("Student Management System")

st.write("Welcome to Student Management System")
BASE_URL = "http://127.0.0.1:8000"
st.write("Click here to see all Student on this class")

# GET all students
def get_all_students():
    response = requests.get(f"{BASE_URL}/all")

    print(response.status_code)
    return response.json()
    #print(type(data))
    #for student in data["status"]:
        #print(student)


if st.button("ALL Student"):

    data = get_all_students()
    students = data["status"]

    # Header
    col1, col2, col3, col4, col5, col6, col7 = st.columns(
        [1, 2, 2, 3, 2, 1, 1]
    )

    col1.write("**Student ID**")
    col2.write("**First Name**")
    col3.write("**Last Name**")
    col4.write("**Email**")
    col5.write("**Phone**")
    col6.write("**Edit**")
    col7.write("**Delete**")

    st.divider()

    # Rows
    for student in students:

        col1, col2, col3, col4, col5, col6, col7 = st.columns(
            [1, 2, 2, 3, 2, 1, 1]
        )

        col1.markdown(f"[{student[0]}](?student_get_detail_id={student[0]})"
                           )
        col2.write(student[1])
        col3.write(student[2])
        col4.write(student[3])
        col5.write(student[4])

        # Edit icon
        if col6.button("✏️", key=f"edit_{student[0]}"):
            st.write(f"Edit student: {student[0]}")

        # Delete icon
        if col7.button("🗑️", key=f"delete_{student[0]}"):
            st.write(f"Delete student: {student[0]}")
def get_student_by_id(student_id:str):

    response = requests.get(
        f"http://127.0.0.1:8000/getbyid/{student_id}"
    )

    if response.status_code == 200:
        return response.json()

    return None
student_get_detail_id = st.query_params.get("student_get_detail_id")
if student_get_detail_id:

    st.title("🎓 Student Details")

    data = get_student_by_id(student_get_detail_id)

    if data:
        student = data["status"]

        st.write(f"### Student ID: {student[0]}")
        st.write(f"**Name:** {student[1]} {student[2]}")
        st.write(f"**Email:** {student[3]}")
        st.write(f"**Phone:** {student[4]}")
        st.write(f"**Gender:** {student[5]}")
        st.write(f"**Date of Birth:** {student[6]}")
        st.write(f"**Address:** {student[7]}")
        st.write(f"**Department:** {student[8]}")
        st.write(f"**Course:** {student[9]}")
        st.write(f"**Admission Date:** {student[10]}")
        st.write(f"**Status:** {student[11]}")
        st.write(f"**Created At:** {student[12]}")
        st.write(f"**Updated At:** {student[13]}")

    else:
        st.error("Student not found")
