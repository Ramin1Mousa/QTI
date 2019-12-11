import streamlit as st
import numpy as np
import pandas as pd

st.title('Applikasi Pertama')
st.write('## Menggunakan Streamlit untuk membangun applikasi')

'''Ini adalah aplikasi pertama saya menggunakan streamlite, gunakan st sebagai nama lain dari streamlit.
Gunakan st.title untuk menulis title dan st.write untuk menulis sebuah paragraf.'''

'''
### Table

Membuat table dalam streamlit dapat dilakukan dengan menggunakan st.write dan memasukan dataframe nya. 

Hasilnya adalah sebagai berikut:
'''

raw_data = pd.DataFrame(
    {
        'Nama' : ['Elga', 'Umar', 'Uga', 'Cayo', 'Agfian', 'Izi'],
        'Umur' : [24, 50, 12, 24, 30, 35]
    }
)

st.write(raw_data)

'''
### Line Chart

Membuat grafik dapat dilakukan dengan menggunakan st.line_chart dan memasukan kolom yang ingin di plot:
'''
st.line_chart(raw_data['Umur'])

'''
### Input Teks

Membuat Input dapat dilakukan dengan menggunakan st.text_input
'''

nama = st.text_input("Masukan Nama Anda di sini: ")

st.write('Selamat datang ', nama, '!')


'''
### Input Numerik

Membuat input numerik dilakukand engan menggunkaan st.number_input
'''
number1 = st.number_input('Masukan input angka pertama ', key='number1')
number2 = st.number_input('Masukan input angka kedua ', key='number2')

if (number1 and number2) != 0:
    st.write('Penjumlahan dua angka tersebut adalah = ', number1+number2)
else:
    st.write('Anda harus memasukan kedua angka input terlebih dahulu!')


'''
### Selector

Membuat selector sederhana menggunakan st.selectbox
'''

hasil_selektor = st.selectbox('Pilih 1 opsi : ', ['Makan', 'Minum', 'Olahraga', 'Tidur'])

st.write('Yang dipilih adalah ', hasil_selektor)

'''
### Multi Select

Membuat multi_select sederhana menggunakan st.multiselect
'''
hasil_multiselect = st.multiselect('Pilih 1 atau beberapa opsi : ', ['Makan', 'Minum', 'Olahraga', 'Tidur'])

st.write('Yang dipilih adalah ', hasil_multiselect)

'''
### Radio Button

Membuat radio sederhana menggunakan st.radio
'''
hasil_radio = st.radio('Pilih 1 opsi : ', ['Makan', 'Minum', 'Olahraga', 'Tidur'])

st.write('Yang dipilih adalah ', hasil_radio)

'''
### Checkbox

Membuat checkbox sederhana menggunakan st.checkbox
'''
hasil_checkbox_makan = st.checkbox('Apakah Anda Lapar?')

if hasil_checkbox_makan:
    st.write('Saya lapar')
else:
    st.write('Saya sudah makan')

'''
### Button

Membuat button sederhana menggunakan st.button
'''

nilai_button = st.button('Klik button')

st.write('Klik button : ', nilai_button)


'''
### Slider

Membuat slider sederhana menggunakan st.slider
'''

nilai_slider = st.slider('Pilih angka menggunakan slider', min_value=0, max_value=10, value=2)

st.write('Nilai dari slider : ', nilai_slider)

'''
### Date Input

Membuat input tanggal sederhana menggunakan st.date_input
'''

nilai_tanggal = st.date_input('Pilih tanggal menggunakan slider')

st.write('tanggal yang Anda pilih : ', nilai_tanggal)

'''
### Time Input

Membuat input waktu sederhana menggunakan st.time_input
'''

nilai_waktu = st.time_input('Pilih waktu menggunakan slider')

st.write('waktu yang Anda pilih : ', nilai_waktu)



