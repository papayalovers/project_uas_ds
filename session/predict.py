import streamlit as st
import pickle 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from . import home

# membaca model
telcom_model = pickle.load(open('./stream_data/telcom_model.sav', 'rb'))

# customer predict session
def do_predict():
    st.header('Customer Churn Prediction :house:', divider='rainbow')

    col1, col2 = st.columns(2)
    # kolom 1
    with col1:
        type_contract = st.selectbox('Contract Type',
        ('Month-to-month','One year','Two year'))

        payment_method = st.selectbox('Select Payment Method',
        ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))

        total_charges = st.text_input('Input Total Charges')

        citizen = st.selectbox('Is Senior Citizen?',
        ('Yes','No'))
        if citizen == 'Yes':
            citizen = 1
        else:
            citizen = 0

        dependents = st.selectbox('Does it Have Dependets?',
        ('Yes','No'))

        mult_lines = st.selectbox('Does it Have Multiple Lines?',
        ('Yes','No'))

    # kolom 2
    with col2:
        paperless_bill = st.selectbox('Is Paperless Billing?',
        ('Yes','No'))

        monthly_charges = st.text_input('Input Monthly Charges')

        gender = st.selectbox('Select Gender',
        ('Male','Female'))

        partner = st.selectbox('Does it Have a Partner?',
        ('Yes','No'))

        internet_services = st.selectbox('Select Internet Services',
        ('DSL', 'Fiber optic', 'No internet Service'))

        total_services = st.selectbox('How Much Services Used?',
        ('0','1','2','3','4','5','6'))


    # code untuk memprediksi customer
    cust_diag= ''

    #
    data_input_new = pd.DataFrame({
        'type' : [type_contract],
        'paperless_billing' : [paperless_bill],
        'payment_method' : [payment_method],
        'monthly_charges' : [monthly_charges],
        'total_charges' : [total_charges],
        'gender' : [gender],
        'senior_citizen' : [citizen],
        'partner' : [partner],
        'dependents' : [dependents],
        'internet_service' : [internet_services],
        'multiple_lines' : [mult_lines],
        'total_services' : [total_services]
        })

    #
    features = home.data.drop(['customer_id','online_backup','tech_support','streaming_movies','online_security','device_protection','streaming_tv','churn'], axis=1)
    numeric_cols = features.describe().columns.to_list()
    categoric_cols = features.describe(include='object').columns.to_list()

    preprocessor = ColumnTransformer(transformers=[
        ('categoric', OneHotEncoder(), categoric_cols),
        ('numeric', MinMaxScaler(), numeric_cols)])

    features_transformed = preprocessor.fit_transform(features)

    # tombol untuk prediksi
    if st.button('Predict Customer'):
        try:
            new_data_transformed = preprocessor.transform(data_input_new)
            cust_prediction = telcom_model.predict(new_data_transformed)

            if cust_prediction[0] == 1:
                cust_diag = 'Ada indikasi bahwa pelanggan akan Churn'
            else:
                cust_diag = 'Tidak ada indikasi bahwa pelanggan akan Churn '

            st.success(cust_diag)
        except:
            e = RuntimeError('Data Tidak Boleh Kosong')
            st.exception(e)
