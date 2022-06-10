#import libraries----------------------------------------------------
import streamlit as st
import pandas as pd

#name of the app-----------------------------------------------------
st.set_page_config(layout="wide")
st.markdown("<h2 style='text-align: center;'>52 Week High & Low</h2>", unsafe_allow_html=True)

#get data from websites----------------------------------------------
high= pd.read_html("https://ticker.finology.in/market/52-week-high")
Hi = high[0]
low = pd.read_html("https://ticker.finology.in/market/52-week-low")
lo = low[0]
data = pd.concat([Hi,lo])

#create text input---------------------------------------------------
st.markdown("<h3 style='text-align: center;'>Enter The Name Of Your Company</h3>", unsafe_allow_html=True)
option = st.text_input("Copy and Paste the Name" ," ")

#if else loop--------------------------------------------------------
if option in Hi.values:
    st.markdown("<h3 style='text-align: center;'>You're Company is in 52 Week High List</h3>", unsafe_allow_html=True)
    st.write("At a Price of ",data.loc[data['Company']==option,"price Rs."].iloc[0])
elif option in lo.values:
    st.markdown("<h3 style='text-align: center;'>You're Company is in 52 Week Low List</h3>", unsafe_allow_html=True)
    st.write("At a Price of ",data.loc[data['Company']==option,"price Rs."].iloc[0])
elif option==" ":
    st.markdown("<h3 style='text-align: center;'></h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align: center;'>your company is not in list</h3>", unsafe_allow_html=True)

# create two columns-------------------------------------------------
col1,col2 = st.columns(2)

#name of dataframes--------------------------------------------------
col1.markdown("<h3 style='text-align: center;'>52 Week High</h3>", unsafe_allow_html=True)
col1.write(Hi)
col2.markdown("<h3 style='text-align: center;'>52 Week Low</h3>", unsafe_allow_html=True)
col2.write(lo)
