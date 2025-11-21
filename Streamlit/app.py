import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as py
#title
st.title("HELLO")

#text
st.write("this is a text ok")

df=pd.DataFrame({
    'fc':[9,17,10,4],
    'lc':[1,7,84,23]
})
st.write(df)
chart_data=pd.DataFrame(df)
st.line_chart(chart_data)