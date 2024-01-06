import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
import session as session

menu_dict = {
    "Summary Of EDA" : {'fn' : session.do_summary},
    "Customer Prediction" : {'fn' : session.do_predict},
    "Profile Report" : {'fn': session.do_home}
}
# 1. as sidebar menu
with st.sidebar:
    # st.subheader('Analysis and :red[Prediction] of :red[Telcom Customer] Churn', divider='gray')
    st.markdown('<h2 style= "text-align: center; padding: 0px 0px 0px">Analysis and Prediction of Telcom <i>Customer Churn</i><h2>', unsafe_allow_html=True)
    st.divider()
    selected = option_menu("Main Menu", ["Profile Report", "Summary Of EDA", 'Customer Prediction'], 
        icons=['house','book', 'list-task'], menu_icon="cast", default_index=0)
    selected

if selected in menu_dict.keys():
    menu_dict[selected]['fn']()
