import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil :')
mileage = st.number_input('Input Km Mobil :')
tax = st.number_input('Input Pajak Mobil :')
mpg = st.number_input('Input Konsumsi BBM Mobil :')
enginSize = st.number_input('Input Engin Size :')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage,tax,mpg,enginSize]]
    )
    st.write ('Estimasi Harga Mobil Bekas Dalam Ponds :', predict)
    st.write ('Estiasi Harga Mobbil Bekas Dalam IDR (Juta) :', predict*19000)