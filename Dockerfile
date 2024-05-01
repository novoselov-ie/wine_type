FROM python:3.11.5

# Установка зависимостей
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Добавление MLflow модели и входных данных JSON
ADD mlruns /app/mlruns
ADD Data_wine.json /app/Data_wine.json

# Копирование исходного кода
ADD WineClassifier.py /app/WineClassifier.py

WORKDIR /app
ENV PYTHONUNBUFFERED=1

CMD [ "python", "./WineClassifier.py" ]