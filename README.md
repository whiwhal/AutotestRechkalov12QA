﻿Задание:

Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:

Клиент создает заказ. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:

Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.Задание:

Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:

Клиент создает заказ. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:

1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.


Автоматизация теста к API 

Скриншот с запуском автотеста.

В папке DiplomYP соодержатся файлы:

1. data.py
Файл с телом запроса для создания нового заказа.

2. configuration.py
Файл с URl стенда, "ручками" создания заказа (/api/v1/orders)

3. sander_stand_request.py
Файл с методами реквестов.

4. Auto_test.py
Файл с автотестом

Для запуска должны быть установлены библиотеки requests и pytest.

Чтобы запустить тест нажмите кнопку Run в файле Auto_test.py.

Работа с базой данных (Папка DataBaseTask)

Папка соодержит:

BDTasks.txt - фйал с запросами, и два скриншота с результатами запросов в командной строке