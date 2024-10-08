# exercis.py - первое задание

# Продуктовый магазин!

## Функционал: 
- регистрация пользователя
- просмотр все товаром
- добавление товаров в корзину
- просмотр и редактирование корзины


## Эндпоинты API

### Регистрация пользователя
`POST /api/users/`  
Регистрация нового пользователя.

### Получение токена
`POST /api/auth/token/login/`  
Получение токена для аутентификации пользователя.

### Отображение каталогов
`GET /api/catalog/`  
Отображение всех каталогов.

### Отображение категорий
`GET /api/categories/`  
Отображение всех категорий.

### Отображение продуктов
`GET /api/products/`  
Отображение всех продуктов.

### Создание корзины
`POST /api/carts/`  
Создание новой корзины.

### Отображение корзины
`GET /api/carts/`  
Отображение всех корзин.

### Изменение корзины
`PATCH /api/carts/1/`  
Изменение корзины с ID 1.

### Удаление элемента корзины
`DELETE /api/carts/1/items/3/`  
Удаление элемента с ID 3 из корзины с ID 1.

## Пример использования

### Регистрация пользователя

```bash
curl -X POST http://127.0.0.1:8000/api/users/ -d '{"username": "your_username", "password": "your_password"}'
```

### Получение токена

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/login/ -d '{"username": "your_username", "password": "your_password"}'
```
