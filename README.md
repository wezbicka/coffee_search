# Ищем, где выбить кофе

Поиск ближайших кофеен в Москве по выбраннной локации

Для расчёта расстояния использовался модуль [GeoPy](https://geopy.readthedocs.io/en/stable/#module-geopy.distance) 

## Требования

Необходимо получить ключ для доступа к [геокодеру Яндекса](https://developer.tech.yandex.ru/).
Подробная инструкция по [Yandex geocoder API](https://devman.org/encyclopedia/api-docs/yandex-geocoder-api/)

Перед использованием получите API ключ в [кабинете разработчика](https://passport.yandex.ru/auth/welcome?origin=apikeys&retpath=https%3A%2F%2Fdeveloper.tech.yandex.ru%2F)

## Переменные окружения

Настройки проекта берутся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ = значение`.

`API_KEY` — ключ для доступа к геокодеру Яндекса.
Пример:

```
API_KEY = ab1234c5-6789-0de1-fgij-2345klmnop
```

## Запуск

Скачайте код с GitHub. Установите зависимости:

```
pip install -r requirements.txt
```

Запустите скрипт:

```
python main.py
```

Пример вывода:

```
Где вы находитесь? Зарядье

 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ```

Теперь нужно запустить браузер и перейти по адресу http://0.0.0.0:5000/.

Вы увидите карту с отмеченными кофейнями:

![alt tag](https://github.com/wezbicka/coffee_search/blob/main/browser.png)

## Цель проекта
Код написан в учебных целях.
