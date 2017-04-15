import sys
import os
from collections import defaultdict


def get_file_name_size_and_paths_dict(path):
    finded_file_name_size_and_paths_dict = defaultdict(list)
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            finded_file_name_size_and_paths_dict['{}_{}'.format(file, file_size)].append(file_path)
    
    return finded_file_name_size_and_paths_dict


def find_duplicates(file_name_size_and_paths_dict):
    return [file_paths for file_paths in file_name_size_and_paths_dict.values() if len(file_paths) > 1]


def input_dir_name_or_exit():
    if len(sys.argv) == 1:
        print('Нет параметров для запуска')
        work_dir = input('Введите имя директории:')
    else:
        work_dir = sys.argv[1]
        if os.path.isdir(work_dir) and os.path.exists(work_dir):
            print('Рабочая директория: {}'.format(work_dir))

    if not os.path.isdir(work_dir):
        print('Указанный путь {} не директория'.format(work_dir))
        sys.exit(1)
    if not os.path.exists(work_dir):
        print('Директория {} не существует'.format(work_dir))
        sys.exit(1)
    
    return work_dir


def print_duplicates(duplicates):
    if duplicates is None:
        print('Дубликаты не найдены')
    else:
        print('Найдены дубликаты:')
        for paths in duplicates:
            print('=' * 80)
            for path in paths:
                print(path)


if __name__ == '__main__':
    dir_name = input_dir_name_or_exit()
    file_name_size_and_paths_dict = get_file_name_size_and_paths_dict(dir_name)
    duplicates = find_duplicates(file_name_size_and_paths_dict)
    print_duplicates(duplicates)
    