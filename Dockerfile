# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /code

# Копируем зависимости в контейнер
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Expose the application on port 8000
EXPOSE 8000

# Run test server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]