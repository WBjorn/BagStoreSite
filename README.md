# Bag Store
* python 3.11
* django 5.0.6

## Клонирование репозитория

Клонируйте репозиторий к себе:
```python
$ git clone https://github.com/ViktorNikolaevichD/BagStoreSite
```

## Установка зависимостей
Установите `poetry`, если ранее он не был установлен:
```python
$ pip install poetry
```
После установки в склонированном репозитории обновите недостающие зависимости:
```python
$ poetry update
```
После этого войдите в виртуальное окружение `poetry`:
```python
$ poetry shell
```

## Добавление недостающих файлов
Если вы используете sqllite, создайте директорию `database` в корне проекта.

Если вы используете другую БД, то в файле `bagstore/bagstore/settings.py` замените `DATABASES` на свою.

Также необходимо добавить в директорию `bagstore/config` добавить файл `.env` и в нем прописать:
- SECRET_KEY="*ваш секретный ключ*"
