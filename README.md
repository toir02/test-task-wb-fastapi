# Тестовое задание Wildberries

Данный сервис реализует простой веб-сервер с вводом-выводом данных.

## Используемые технологи
- python
- fastapi
- postgres
- alembic
- docker
- docker-compose

## Как запустить этот проект локально?

- Убедитесь, что у вас установлен docker и docker-compose
- Склонируйте репозиторий и перейдите в директорию

  В терминале ввести команды:
  
  ```
  git clone https://github.com/toir02/test-task-wb-fastapi
  cd test-task-wb-fastapi/
  ```

- Создать файл `.env` и заполнить его данными на основе файла ``.env.sample``
- 
- Запустить проект

  В терминале ввести команду:

  ```
  docker-compose up --build
  ```

## API эндпоинты

Для обращения к API реализовано несколько эндпоинтов, принимающие запросы GET или POST.

```
http://0.0.0.0:8080/record/
```
Данный эндпоинт принимает POST запрос со следующими параметрами:

```
{
    "data": {
        some data
    }
}
```
И возвращает объект с уникальным идентификатором(id).

```
http://0.0.0.0:8080/records/
```
Данный эндпоинт принимает GET запрос и выдает все записи в базе данных с пагинацией.

Возможные query-параметры:

page - номер страницы, по умолчанию 1

page_size - колчиество объектов, отображаемое на одной странице, по умолчанию 10, масимально возможное 100.

```
http://0.0.0.0:8080/record/{record_id}/
```
Данный эндпоинт принимает GET запрос и возвращает детально запись в базе данных по передаваемому уникальному идентификатору.

## Документация

Документация к проекту доступна на следующих адресах:

```
http://0.0.0.0:8080/docs/
http://0.0.0.0:8080/redoc/
```