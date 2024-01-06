from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pickle
import streamlit as st

# membaca data
with open("./stream_data/used_data.pickle",'rb') as file:
    data = pickle.load(file)

# home session
def do_home():
    st.header('Telcome Profile Report :house:', divider='rainbow')
    profile = ProfileReport(data, title='Telcom Data Profile Report', html={'style':{'full_width':True}})
    st_profile_report(profile)