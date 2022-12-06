from ast import If
import pickle
import streamlit as st

#Membaca Model
anemia_model = pickle.load(open('anemia_model.sav', 'rb'))

#Judul Web
st.title('DATA MINING PREDIKSI ANEMIA')

st.subheader('NAMA : RIZAN RAMDANI')
st.subheader('NIM : 191351080')

Gender = st.text_input('GENDER [1=fEMALE, 0=MALE]')

Hemoglobin = st.text_input ('Input Nilai HEMOGLOBIN')

MCH = st.text_input (' Input Nilai MCH')

MCHC = st.text_input ('Input Nilai MCHC')

MVC = st.text_input (' Input Nilai MVC')

#code untuk prediksi
anem_diagnosis = ''

#membuat tombol
if st.button('Test') :
    anemia_prediction = anemia_model.predict([[Gender, Hemoglobin, MCH, MCHC, MVC]])
    
    if  (anemia_prediction[0] == 1):
           anem_diagnosis = 'Pasien terkena Anemia'
    else :
           anem_diagnosis = ' Pasien tidak terkena Anemia'

    st.success(anem_diagnosis)