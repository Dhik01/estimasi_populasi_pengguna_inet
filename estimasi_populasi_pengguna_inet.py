import pickle
import streamlit as st

model = pickle.load(open('estimasi_populasi_pengguna_inet.sav', 'rb'))

st.title('Estimasi Persentase Populasi Pengguna Internet Diseluruh Dunia Tahun 1980-2020')

Cellular_Subscription = st.number_input('Input nilai jumlah pelanggan layanan seluler :')
No_of_Internet_Users = st.number_input('Input nilai jumlah pengguna internet diseluruh dunia :')
Broadband_Subscription = st.number_input('Input nilai jumlah pelanggan internet broadband :')
Year = st.number_input('Input tahun populasi pengguna internet (1980-2020) :')

predict = ''

if st.button('Estimasi persentase populasi pengguna internet'):
    predict = model.predict(
        [[Cellular_Subscription, No_of_Internet_Users, Broadband_Subscription, Year]]
    )
    st.write ('Estimasi persentase populasi pengguna internet diseluruh dunia (%) : ', predict)
