"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [{'name': 'John Marston', 'age': 38, 'job': 'cowboy'},
            {'name': 'John Shepard', 'age': 55, 'job': 'commander'},
            {'name': 'Billie Milligan', 'age': 30, 'job': 'anything'},
            {'name': 'Tony Stark', 'age': 50, 'job': 'engineer'},
            {'name': 'Patrick Star', 'age': 41, 'job': 'superstar'},
            {'name': 'Elizabeth the Second', 'age': 99, 'job': 'wizard'}]
    columns = ['name', 'age', 'job']
    
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main()
