# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:08:00 2026

@author: Admin
"""
import streamlit as st

st.title("Student Management System")

st.write("Welcome to Student Management System")

name = st.text_input("Enter Student Name")

if st.button("Submit"):
    st.write("Student Name:", name)

