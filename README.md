# Yatube API

### Описание
Программный интерфейс для работы с блог-платформой Yatube.  
Варианты взаимодействия с ресурсами:
- передача логина и пароля и получение токена пользователя;
- получение списка публикаций или создание новой публикации;
- получение, редактирование, удаление публикации по id;
- получение списка всех сообществ;
- получение информации о сообществе по id;
- получение списка всех комментариев к публикации или создание нового комментария;
- получение, редактирование, удаление комментария;
- получение всех подписок пользователя, сделавшего запрос;
- создание подписки.

### Технологии
- Python 3.8.9
- Django 2.2.16

### Запуск проекта в dev-режиме
- Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://github.com/marusya-zh/api_final_yatube.git
```
```
cd api_final_yatube
```
- Установите и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Выполните миграции:
```
python3 manage.py migrate
```
- Находясь в папке с файлом manage.py, запустите проект командой:
```
python3 manage.py runserver
```

### Примеры запросов

Получение токена.

```POST /api/v1/jwt/create/```

request sample
```
{
    "username": "string",
    "password": "string"
}
```

response sample
```
{
    "refresh": "string",
    "access": "string"
}
```

Создание публикации.

```POST /api/v1/posts/```

request sample
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

response sample
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-12-21T13:15:22Z",
    "image": "string",
    "group": 0
}
```

Получение списка сообществ.

```GET /api/v1/groups/```

response sample
```
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```

Обновление комментария.

```PUT /api/v1/posts/{post_id}/comments/{id}/```

request sample
```
{
    "text": "string"
}
```

response sample
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2021-12-21T13:15:22Z",
    "post": 0
}
```

### Автор
Mariya Zhuchina
