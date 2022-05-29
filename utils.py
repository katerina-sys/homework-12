import json

from exceptions import DataSourceBrokenException


def json_load():
    """Загружает данные из файла"""
    try:
        with open('posts.json', 'r', encoding='UTF-8') as f:
            file = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataSourceBrokenException("Файл с данными поврежден")

    return file


def search_post(item):
    """Добавляет в хранилище постов определенный пост"""
    list_post = []
    for post in json_load():
        if item in post['content']:
            list_post.append(post)

    return list_post


def save_data(data):
    """Перезаписывает переданные данные в файле с данными"""
    with open('posts.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False)


def get_all():
    """Отдает полный список данных"""
    data = json_load()
    return data


def search(substring):
    """Отдаёт посты, которые содержат substring"""
    posts = json_load()
    substring = substring.lower()

    all_posts = [post for post in posts if substring in post["content"].lower()]

    return all_posts
