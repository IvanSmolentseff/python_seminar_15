'''Задание №6
📌 Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя
логирование.'''

import logging
import argparse
import os
from collections import namedtuple

logging.basicConfig(filename='log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Принимаем строку с путём до директории.")
parser.add_argument("dir_path", nargs="?", type=str,
                    help="Указать путь к папке. "
                         "Если в написании пути имеются пробелы - используйте двойные кавычки.")

args = parser.parse_args()

if not args.dir_path:
    parser.error("Путь к папке не был передан!"
                 "\nПожалуйста, повторите попытку.")
elif os.path.exists(args.dir_path):
    print(args)
else:
    parser.error("Указанный путь к папке не существует!"
                 "\nПожалуйста, проверьте правильность введенного пути и повторите попытку.")

data_list = [(dirs, folders, files) for dirs, folders, files in
             os.walk(args.dir_path)]
# print(*data_list)
clas_list = []

Data = namedtuple('Data',
                  ['file_name', 'file_exten', 'dir_flag', 'parent_dir'])
for i in range(0, len(data_list)):
    parent_dir = data_list[i][0]
    dir_list = data_list[i][1]
    file_list = data_list[i][2]

    for el in dir_list:
        dir_flag = 'Yes'
        file_name = el
        file_exten = ''
        d = Data(file_name, file_exten, dir_flag, parent_dir)
        clas_list.append(d)
        logger.info(
            f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

    for item in file_list:
        dir_flag = 'No'
        try:
            file_name, file_exten = item.split('.')
        except Exception:
            *file_name, file_exten = item.split('.')

        d = Data(file_name, file_exten, dir_flag, parent_dir)
        clas_list.append(d)
        logger.info(
            f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

print(*clas_list, sep="\n")
