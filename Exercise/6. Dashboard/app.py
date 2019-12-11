import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import eli5
from yellowbrick.regressor import PredictionError, ResidualsPlot

model_lr = pickle.load(open('model_lr.sav', 'rb'))
X_train = pickle.load(open('X_train.sav', 'rb'))
y_train = pickle.load(open('y_train.sav', 'rb'))
X_test = pickle.load(open('X_test.sav', 'rb'))
y_test = pickle.load(open('y_test.sav', 'rb'))
y_pred = model_lr.predict(X_test)

st.title('House Price Prediction')
st.image('960x0.jpg', use_column_width=True)

st.markdown('''
Aplikasi ini berfungsi untuk melakukan prediksi dari harga sebuah rumah menggunakan 
model Regresi Linear. Model di-training dengan menggunakan dataset "*House Prices: Advanced Regression Techniques*" yang didapatkan dari Kaggle.
''')

st.markdown('''
Tidak semua kolom digunakan dalam aplikasi ini. Kolom yang 
digunakan antara lain:

**1. OverallQual**
> Rate dari keseluruhan material dan kondisi rumah. Bernilai antara 1 sampai dengan 10. 
Nilai 1 menunjukan nilai terburuk sedangkan nilai 10 menunjukan nilai yang terbaik.

**2. GrLivArea**
> Luas dari rumah yang diprediksi dalam satuan *square feet*. 

**3. GarageArea**
> Luas dari garasi rumah yang diprediksi dalam satuan *square feet*. Akan bernilai 0 apabila rumah yang diprediksi tidak memiliki garasi.

**4. GarageCars**
> Luas dari garasi rumah dengan satuan jumlah mobil yang dapat masuk ke dalam garasi. Memiliki rentang nilai 0 - 4. Akan bernilai 0 apabila rumah yang diprediksi tidak memiliki garasi.

**5. 1stFlrSF**
> Luas dari lantai pertama dalam satuan *square feet*.

**6. ExterQual**
> Evaluasi dari material eksterior dari rumah. Terdiri dari beberapa kategori yaitu `Ex` untuk `Excellent`,
`Gd` untuk `Good`, `TA` untuk `Average/Typical`, dan `Fa` untuk `Fair`.

''')

'''
## Prediksi

Prediksi harga rumah dapat dilakukan dengan cara mengisi form di bawah ini:
'''
st.write('')

# INPUT DATA
OverallQual = st.slider('OverallQual', min_value=1, max_value=10, value=1)

GrLivArea = st.number_input('GrLivArea (dalam square feet)', key='GrLivArea')

GarageArea = st.number_input('GarageArea (dalam square feet)', key='GarageArea')

GarageCars = st.slider('GarageCars ', min_value=0, max_value=4, value=0)

firstFlrSF = st.number_input('1stFlrSF (dalam square feet)', key='firstFlrSF')

ExterQual = st.selectbox('ExterQual ', ['Ex', 'Gd', 'TA', 'Fa'])


if ExterQual == 'Ex':
    ExterQual_Ex = 1
    ExterQual_Gd = 0
    ExterQual_TA = 0
    ExterQual_Fa = 0
elif ExterQual == 'Gd':
    ExterQual_Gd = 1
    ExterQual_Ex = 0
    ExterQual_TA = 0
    ExterQual_Fa = 0
elif ExterQual == 'TA':
    ExterQual_TA = 1
    ExterQual_Gd = 0
    ExterQual_Ex = 0
    ExterQual_Fa = 0
else:
    ExterQual_Fa = 1
    ExterQual_Gd = 0
    ExterQual_TA = 0
    ExterQual_Ex = 0
# INPUT DATA ENDS HERE

# PREDICTION PROCESS
to_predict = [OverallQual, np.log(GrLivArea + 1), GarageArea, GarageCars, np.log(firstFlrSF + 1) , ExterQual_Ex, ExterQual_Fa, ExterQual_Gd, ExterQual_TA]

prediction = model_lr.predict([to_predict])

harga_prediksi = np.exp(prediction) - 1
# PREDICTION PROCESS ENDS HERE

'''
Hasil Prediksi Harga Rumah: 
'''
st.write('$ ', round(harga_prediksi[0], 2))

'''
## Model Explanation
'''

'''
#### 1. Weight dan Bias
'''
st.write('')
feature_names = X_train.columns.to_list()
st.write(eli5.formatters.as_dataframe.explain_weights_df(estimator=model_lr, feature_names=feature_names)[['feature', 'weight']])

'''
Koefisien yang paling besar dari model adalah GrLivArea sebesar 0.3154, artinya harga rumah sensitif dengan kolom ini. Apabila
terjadi peningkatan terhadap nilai GrLivArea, harga rumah akan meningkat lebih tinggi dibandingkan apabila terjadi kenaikan pada feature yang lain dengan kenaikan yang sama.
Perhatikan juga terdapat feature dengan nilai koefisien yang negatif (ExterQual_TA dan ExterQual_Fa), artinya apabila feature ini meningkat maka harga rumah akan menjadi lebih turun.
'''

'''
#### 2. Residual Plot
'''
st.write('')
visualizer_residual = ResidualsPlot(model_lr)
visualizer_residual.fit(X_train, y_train)
visualizer_residual.score(X_test, y_test)
visualizer_residual.finalize()

st.pyplot()
'''
Residual berdistribusi paling banyak pada nilai 0. Akan tetapi, masih terdapat nilai residual yang cukup tinggi. Hal ini menyebabkan distribusi dari residual tidak sepenuhnya normal, tetapi menjadi skew.
'''

'''
#### 3. Prediction Error
'''

st.write('')
visualizer_prediction_error = PredictionError(model_lr)
visualizer_prediction_error.fit(X_train, y_train)
visualizer_prediction_error.score(X_test, y_test)
visualizer_prediction_error.finalize()

st.pyplot()

'''
Antara garis best fit dengan garis identity tidak begitu jauh, sehingga dapat dikatakan bahwa model yang dibuat optimal.
'''