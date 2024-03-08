# Django REST и API - реализация работы склада


**Сущности:**
* User (пользователь)
* Product (товар) 
* Storage (склад)

**Права пользователей:**
* Суперюзер имеет все права на все сущности
* На объекты User - все могут просматривать, добавлять; редактировать/удалять может только владелец или суперюзер;
* На объекты Storage - все могут просматривать; редактировать/удалять может только суперюзер;
* На объекты Products - все могут просматривать; редактировать могут (**количество должно быть положительным**):
    * Поставщик может поставлять товар (увеличивать поле Количество) и менять склад (поле Склад)
    * Потребитель может забирать товар (уменьшать поле Количество)
    * Суперюзер может менять все поля
* Реализована аутентификация пользователей по паролю или токену


**Создание виртуального окружения:** python -m venv venv

**Компиляция зависимостей из requirements.in в requirements.txt:** pip-compile

**Установка зависимостей из requirements.txt:** pip-sync

**Создание миграций:** python manage.py makemigrations

**Применение миграций:** python manage.py migrate


* Регистрация пользователя реализована по email и паролю с указанием типа 'поставщик', 'потребитель'
  (т.к. регистрация по email, а не username, в классе User поле username отключено, соответственно, 
создать суперюзера стандартной командой createsuperuser не получится, для этого используется команда см. ниже):

**Создание суперюзера:** python manage.py csu  (параметры - в файле \management\commands\csu.py)

**Запуск проекта:** python manage.py runserver 

http://127.0.0.1:8000/ - интерфейс API после запуска

http://127.0.0.1:8000/users/ - интерфейс для работы с пользователями

http://127.0.0.1:8000/storages/  - интерфейс для работы со складами

http://127.0.0.1:8000/products/ -  интерфейс для работы с товарами


* docker build -t drf:1 . - создание образа drf с тэгом 1 из Dockerfile
* docker run --rm -it -p 8000:8000 drf:1 - запустить образ