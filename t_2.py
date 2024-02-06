'''Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним
логирование ошибок и полезной информации. Также реализуйте возможность запуска
из командной строки с передачей параметров.

P.S. На семинаре вы посоветовали использовать первую задачу из семинара.
'''

import argparse
import logging

logging.basicConfig(filename='log_2.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} функция "{funcName}()"'
                           ' строка {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Принимаем два целых числа.")
parser.add_argument("a", type=int, help="Делимое - введите целое число")
parser.add_argument("b", type=int, help="Делитель - введите целое число")

args = parser.parse_args()

def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return None
    logger.info(f'{a} / {b} = {res}')
    return res


if __name__ == '__main__':
    print(f'{division(args.a, args.b)}')
