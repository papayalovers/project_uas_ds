import streamlit as st
from . import home
import plotly.graph_objects as go
import plotly.express as px

# eda summary session
def do_summary():
    colors = ["gold", "mediumturquoise", "darkorange", "lightgreen"]
    st.header('Summary Of Exploratory Data Analysis (EDA)', divider='rainbow')
    st.markdown("<p style='text-align: justify;'> Customer Churn didefinisikan sebagai kecenderungan pelanggan untuk berhenti menggunakan layanan atau berpindah ke perusahaan pesaing. Berdasarkan data yang diterima, sebanyak 26.6% pelanggan yang telah churn dari perusahaan telekomunikasi. Bisa diperhatikan seperti dibawah ini:</p>", unsafe_allow_html=True)
    churn_data = home.data['churn'].value_counts()
    churn_fig = go.Figure(data=[go.Pie(labels=churn_data.index, values=churn_data.values, hole=.2, pull=[0,0.1])])
    st.markdown('<h5 style="text-align: justify;">Total Churn By Customer</h5>', unsafe_allow_html=True)
    st.plotly_chart(churn_fig, theme="streamlit")
    #
    st.markdown("<p style='text-align: justify;'>Setelah melakukan analisis terhadap perilaku pelanggan. Terdapat dua kategori yang dapat menggambarkan pola atau tren terkait pelanggan yang beralih (churn) dan diharapkan bisa memberikan solusi dalam pengambilan keputusan selanjutnya.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>Berikut ini adalah kecenderungan pelanggan yang memilih untuk <b>Churn:</p>", unsafe_allow_html=True)
    contract_data = home.data.groupby(['type','churn'])['type'].value_counts().reset_index()
    contract_fig = px.histogram(contract_data, x="type", y="count", color='churn', barmode='group', height=400)
    st.markdown('<h5 style="text-align: justify;">1. Churn By Contract Type</h5>', unsafe_allow_html=True)
    st.plotly_chart(contract_fig, use_container_width=True, height=200, theme=None)
    st.markdown("<p style='text-align: justify;'>Berdasarkan diagram batang diatas, kita bisa memperhatikan bahwa pelanggan yang cenderung <i>churn</i> dan jumlahnya paling banyak diantara kategori lain yaitu pelanggan yang dengan jenis kontrak layanan <i>Month-to-month</i>.</p>", unsafe_allow_html=True)
    #
    total_services_data = home.data.groupby(['total_services','churn'])['type'].count().reset_index()
    # total_services_data_fig = px.bar(total_services_data, x="total_services", y="type", color='churn', barmode='group', height=400, title='2. Churn By Total Services')
    total_services_data_fig = go.Figure(data=[
        go.Bar(name=total_services_data.query('churn == 1')['churn'].unique()[0].astype('str'), x=total_services_data.query('churn == 1')['total_services'], y=total_services_data.query('churn == 1')['type']),
        go.Bar(name=total_services_data.query('churn == 0')['churn'].unique()[0].astype('str'), x=total_services_data.query('churn == 0')['total_services'], y=total_services_data.query('churn == 0')['type'])
    ])
    st.markdown('<h5 style="text-align: justify;">2. Churn By Total Services</h5>', unsafe_allow_html=True)
    total_services_data_fig.update_layout(barmode='group')
    st.plotly_chart(total_services_data_fig, use_container_width=True, theme='streamlit')
    st.markdown("<p style='text-align: justify;'>Kemudian berdasarkan total services, kita bisa memperhatikan bahwa pelanggan yang cenderung churn biasanya menggunakan layanan atau services yang sedikit dan semakin banyak layanan yang digunakan oleh pelanggan, maka semakin kecil pula tingkat churn-nya.</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: justify;'>Conclusion</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>Setelah melakukan tahapan <i>Exploratory Data Analysis</i> (EDA). Ada beberapa kesimpulan yang dapat diambil:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>1. <b>Proporsi Churn Pelanggan</b>: Ditemukan bahwa sekitar 26.6% dari total pelanggan telah beralih dari layanan yang diberikan oleh perusahaan. Angka ini cukup besar dan hal ini merupakan sebuah tantangan bagi perusahaan untuk mempertahankan pelanggan.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>2. <b>Jenis Kontrak Pengguna</b>: Mayoritas pelanggan yang cenderung untuk berpindah (churn) adalah mereka yang menggunakan jenis kontrak layanan <i>Month-to-month</i>. Hal ini menyoroti perlunya peninjauan lebih lanjut terkait kebijakan kontrak dan strategi retensi untuk segmen ini.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>3. <b>Keterkaitan dengan Total Layanan yang Digunakan</b>: Terdapat hubungan yang jelas antara jumlah layanan yang digunakan oleh pelanggan dengan tingkat churn. Pelanggan yang menggunakan sedikit layanan cenderung memiliki tingkat churn yang lebih tinggi, sementara pelanggan dengan lebih banyak layanan cenderung lebih setia.</p>", unsafe_allow_html=True)


