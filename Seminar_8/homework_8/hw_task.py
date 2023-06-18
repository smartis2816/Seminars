# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pathlib
import pickle


def bypass_dir(directory):
    objects = list(os.walk(directory))
    result = []
    for obj in objects:
        temp = {'Название': os.path.basename(obj[0]), 'Тип': 'директория',
                'Родительская папка': os.path.dirname(obj[0]), 'Размер': get_size_dir(obj[0]),
                'Содержит папки': [], 'Содержит файлы': []}
        for folder in obj[1]:
            dir_path = os.path.join(obj[0], folder)
            temp['Содержит папки'].append({'Название': folder, 'Тип': 'директория',
                                           'Размер': get_size_dir(dir_path)})
        for file in obj[2]:
            file_path = os.path.join(obj[0], file)
            temp['Содержит файлы'].append({'Название': file, 'Тип': 'файл',
                                           'Размер': os.path.getsize(file_path)})
        result.append(temp)
    return result


def convert_to_json(data):
    with open("directory_traversal.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=3)


def convert_to_csv(data):
    head = ('Название', 'Тип', 'Родительская папка', 'Размер', 'Содержит папки', 'Содержит файлы')
    with open("directory_traversal.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(head)
        for item in data:
            writer.writerow((item['Название'], item['Тип'], item['Родительская папка'], item['Размер'],
                             item['Содержит папки'], item['Содержит файлы']))


def convert_to_pickle(data):
    with open("directory_traversal.pickle", 'wb') as f:
        pickle.dump(data, f)


def get_size_dir(directory):
    size = 0
    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_file():
                size += entry.stat().st_size
            elif entry.is_dir():
                size += get_size_dir(entry.path)
    return size


