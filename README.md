# Платформа онлайн-обучения

Веб-приложение для управления курсами, уроками, пользователями и платежами с интеграцией Stripe, кешированием и фоновыми задачами Celery.

## Основной функционал

- Управление курсами и уроками (CRUD через DRF).
- Разграничение прав: обычные пользователи, модераторы, владельцы.
- Регистрация, аутентификация (JWT), восстановление пароля.
- Подписка на обновления курса.
- Интеграция с Stripe для оплаты курсов и уроков.
- Кеширование страниц (Redis).
- Фоновые задачи Celery:
  - Отправка уведомлений подписчикам при обновлении курса.
  - Блокировка неактивных пользователей (если не заходили > 30 дней).
- Документация API (drf-spectacular).

## Структура проекта
``` 
online_learning_platform/
├── config/ # Настройки проекта
│ ├── init.py
│ ├── asgi.py
│ ├── celery.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── materials/ # Приложение с курсами и уроками
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── paginations.py
│ ├── serializers.py
│ ├── tasks.py
│ ├── tests.py
│ ├── urls.py
│ ├── validations.py
│ └── views.py
├── users/ # Приложение пользователей
│ ├── fixtures/
│ │ ├── groups_fixture.json
│ │ └── users_fixture.json
│ ├── management/commands/
│ │ ├── init.py
│ │ └── csu.py
│ ├── migrations/
│ ├── templates/
│ │ └── users/
│ │ ├── login.html
│ │ └── payment_success_url.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── permissions.py
│ ├── serializers.py
│ ├── services.py
│ ├── tasks.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── .env
├── .gitignore
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Установка и запуск

1. **Клонирование и переход в директорию**

2. **Установка зависимостей (Poetry):**
``` 
poetry install
```

3. **Настройка переменных окружения:**
- Скопируйте `.env.sample` в `.env`
- Заполните параметры базы данных, почты, Stripe, Redis

4. **Применение миграций и создание суперпользователя:**
``` 
python manage.py migrate
python manage.py csu
```

5. **Установка и запуск Redis (если не запущен):**
```
poetry add redis
redis-server 
```

6. **Запуск Celery worker и beat:**
``` 
celery -A config worker --loglevel=info -P eventlet  # для Windows. Для остальных без eventlet
celery -A config beat --loglevel=info
```

7. **Запуск сервера:**
``` 
python manage.py runserver
```

## Функциональности

### Пользователи и права

- Регистрация, вход, выход, восстановление пароля.
- Аутентификация через JWT (API).
- Роли:
- **Обычный пользователь** — без созданных объектов не имеет прав ни на что.
- **Владелец** — редактирует и удаляет только свои объекты.
- **Модератор** — просматривает и редактирует любые курсы и уроки (но не может создавать или удалять).

### Курсы и уроки

- CRUD через DRF.
- Валидация ссылок на видео (только YouTube).
- Пагинация (5 записей на страницу, можно менять).
- При обновлении курса подписчикам отправляется уведомление (Celery).

### Подписки

- Пользователь может подписаться на курс.
- При обновлении курса подписчикам приходит письмо.
- В сериализаторе курса есть поле `is_subscribed` — показывает, подписан ли текущий пользователь.

### Платежи (Stripe)

- Оплата курсов и уроков через Stripe.
- Создание продукта, цены и сессии в Stripe.
- Сохранение ID сессии и ссылки на оплату в модели `Payment`.
- После успешной оплаты пользователь перенаправляется на страницу успеха.

### Кеширование

- Серверное кеширование страниц (Redis).
- Клиентское кеширование статики.

### Фоновые задачи (Celery)

- `mailing_for_updates` — отправка писем подписчикам при обновлении курса.
- `block_inactive_users` — блокировка пользователей, не заходивших более 30 дней (выполняется раз в сутки).

### API-документация

- Swagger UI: `/swagger-ui/`
- Redoc: `/redoc/`

## Инструменты

- Python 3.13
- Django 6.0.6
- Django REST Framework 3.17.1
- django-filter 25.2
- djangorestframework-simplejwt 5.5.1
- drf-spectacular 0.29.0
- PostgreSQL (psycopg2-binary 2.9.12)
- Redis 4.6.0
- Celery 5.6.3 + eventlet 0.41.0
- Stripe API 15.3.0
- python-dotenv 1.2.2
- Pillow 12.2.0
- coverage 7.14.3
- ipython 9.14.1
- django-celery-beat 2.9.0
- Poetry
