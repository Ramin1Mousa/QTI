import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


raw_data = pd.read_csv('train.csv')

column = [col for col in raw_data.columns]

'''
# Aplikasi untuk menampilkan data

'''

'''
Pilih kolom yang Anda ingin lihat dalam tabel. Pilihlah satu atau beberapa kolom, jika tidak diisi maka akan menunjukkan seluruh kolom 
yang terdapat di dalam dataset
'''
hasil_multiselect = st.multiselect('Pilih kolom :', column)

if len(hasil_multiselect) != 0:
    column_to_see = hasil_multiselect
else:
    column_to_see = column

'''
Pilih jumlah baris yang ingin Anda lihat. Jumlah tersebut adalah jumlah baris pertama dari dataset.
'''
number1 = st.number_input('Masukan jumlah baris ', key='number1')
'''
## Hasil Tabel dari Query Anda
'''
if number1 > len(raw_data):
    st.write('Anda tidak dapat melihat tabel lebih dari jumlah data yang ada yaitu ', len(raw_data))
else:
    st.write(raw_data[column_to_see].head(number1))


'''
## Rata-rata Harga Keseluruhan Data Berdasarkan YrBuilt
'''

saleprice_groupby_yrbuilt = raw_data.groupby('YearBuilt').mean()['SalePrice']

fig = go.Figure(data=go.Scatter(x=saleprice_groupby_yrbuilt.index, y=saleprice_groupby_yrbuilt.values))
fig.update_layout(title='SalePrice grouped by YearBuilt',
                   xaxis_title='YearBuilt',
                   yaxis_title='Average SalePrice')

st.write(fig)
