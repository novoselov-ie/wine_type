import torch
import pandas as pd
import json

from art import tprint
from tqdm import tqdm
import mlflow

tprint("Wine_Classifier")

def compare_cols(row):
    if row[0] > row[1]:
        return 0
    else:
        return 1

logged_model = f"runs:/e7988002ae554cb4a3e9c5705712f28f/model"
loaded_model = mlflow.pyfunc.load_model(logged_model)

PATH_X_data = './Data_wine.json'
X_test = pd.read_json(PATH_X_data, orient='split')

print('Загрузка данных выполнена успешно!\n')

outputs = loaded_model.predict(X_test)
df = outputs.apply(compare_cols, axis=1)

#Экспорт данных в json файл
predicted_list = ['red' if value == 1 else 'white' for value in df]
with open('predicted_data.json', 'w') as f:
    json.dump(predicted_list, f)

print('\n\nПредсказанные значения сохранены в файл "predicted_data.json"')
