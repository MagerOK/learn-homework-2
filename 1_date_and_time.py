"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    month_ago = today - timedelta(days=30)
    print(today.strftime('%d/%m/%Y %H:%M'))
    print(yesterday.strftime('%d/%m/%Y %H:%M'))
    print(month_ago.strftime('%d/%m/%Y %H:%M'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date)
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
