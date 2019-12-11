from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import ast
import pickle
import numpy as np

app = FastAPI()

data = pd.read_csv('train.csv')
model = pickle.load(open('model_lr.sav', 'rb'))


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get('/list_col')
def get_list_col():
    column_list = data.columns
    return column_list.to_dict()

@app.get('/column/{column_name}')
def get_from_column(column_name: str, number_row: int = 5):
    hasil_query = data[column_name].head(number_row)
    return hasil_query.to_dict()

@app.get('/several_col/{column_name}')
def get_from_column(column_name: str, number_row: int = 5):
    columns_list = ast.literal_eval(column_name)
    hasil_query = data[columns_list].head(number_row)
    return hasil_query.to_dict()

@app.get('/prediction')
def get_prediction(OverallQual: int = 1, GrLivArea: int = 0, GarageArea: int = 0, GarageCars: int = 0, firstFlrSF: int = 0, ExterQual : str = 'TA'):
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
    
    predict_list = [OverallQual, np.log(GrLivArea + 1), GarageArea, GarageCars, np.log(firstFlrSF+1), ExterQual_Ex, ExterQual_Fa, ExterQual_Gd, ExterQual_TA]

    prediction = model.predict([predict_list])

    return f'Hasil Prediksi {round(np.exp(prediction[0]) - 1, 2)}'
