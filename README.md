# Wine Classifier

## Описание
Этот проект представляет собой небольшой проект машинного обучения, который использует данные о составе вина для определения его типа (красное или белое). Для этого используются такие признаки, как "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol" и "quality". Модель обучается на этих данных и сохраняет предсказанные типы вина в файл `predicted_data` в формате `json`.

## Установка
1. Установите необходимые библиотеки с помощью команды:
    ```
    pip install -r requirements.txt
    ```

## Использование
1. Выполните предсказания, используя файл `WineClassifier.py`.
    ```
    python WineClassifier.py
    ```
   Этот скрипт загрузит обученную модель из MLflow и выполнит предсказания на тестовых данных.


## Структура проекта
- `WineClassifier.py`: Скрипт для загрузки обученной модели из MLflow и выполнения предсказаний на тестовых данных.
- `requirements.txt`: Файл с зависимостями проекта.
- `predicted_data.json`: Файл, в который сохраняются предсказанные типы вина.
- `Dockerfile`: Файл для сборки Docker-контейнера.
- `Original_wine_type.json`: Оригинальные данные о цвете вина.
- `mlruns/`: Папка, содержащая данные о модели и обучении, сохраненные в MLflow.
- `Data_wine.json`: Тестовые данные для выполнения предсказаний.

## Успешное выполнение программы
![Output](https://github.com/novoselov-ie/wine_type/blob/main/img/Example.png)


## Зависимости
- Python 3.11
- PyTorch
- Pandas
- Tqdm
- Art
- Numpy
- MLflow
