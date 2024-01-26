from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    curr=conn.cursor()
    curr.execute(sql)
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt =[
    """
     You are an expert in converting English question to SQL query!
     The Sql Database has the name STUDENT and has the following columns - NAME, CLASS,
     SECTION and MARKS \n\nFor example 1- How many entries of  records are present
     the SQL command will be something like this  SELECT COUNT (*) STUDENT ;
     \n Example2 - Tell me all the student studying in data science class?,
     the SQL command will be something like this SELECT * FROM STUDENT  
     where CLASS="DATA SCIENCE";
     also the SQL code should not have ``` in begining or end and sql word in output
"""
]

st.set_page_config(page_title="I can retreive any SQL query")
st.header("Gemini App to retreive SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked 
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)