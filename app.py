from dotenv import load_dotenv

load_dotenv()  # loads all environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure teh genai key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


# Function to load Google Gemini Model and provides queries and response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')  # ----------------------------may this line can give you error
    response = model.generate_content(([prompt[0], question]))
    return response.text


# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION For example,Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

# Streamlit App
st.set_page_config(page_title="Retrieve any SQL query")
st.header('Retrieve the sql data using gemini')

question = st.text_input('Input', key='input')
submit = st.button('Send the Querry')

# if Submit button is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, 'student.db')
    st.subheader('The Response is: ')
    for row in response:
        print(row)
        st.header(row)
