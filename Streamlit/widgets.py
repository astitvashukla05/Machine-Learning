import streamlit as st
st.title("Text Inputt")

name=st.text_input('What is you name')
age=st.slider('Select you age',10,100,25 )
options=['py','c','c++','java']
select=st.selectbox('Select you language',options)
if name:
    st.write(f"Hello {name}")
    st.write(f"So you are {age} year old")


uplaod_file=st.file_uploader('Chose a csv file',type="csv")