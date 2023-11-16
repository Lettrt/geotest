# geotest
# Запуск проекта через докер
Установка виртуального окружения
```angular2htm
python3 -m venv venv
```
Активация виртуального окружения
```bash
source venv/bin/activate
```
Установка зависимостей
```bash
pip install -r requirements.txt
```
Так же понадобится создать файл .env
```env
DEBUG=False
SECRET_KEY=(ваш ключ проека)
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
ALLOWED_HOSTS=*
```
Запуск docker контейнера:
- celery & redis уже в контейнере

```bash
docker-compose up --build
```
Применить миграции 

```bash
docker exec -i имя контейнера python3 manage.py migrate
```

Покрытие тестами 90% (pytest)
