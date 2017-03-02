import sys

from url_sh import storage
conn = storage.connect()
storage.initialize(conn)


def action_find_all():
    #в скобках глобальная переменная - объект соединения
    urls = storage.find_all(conn)

    for url in urls:

        print('{url[short_url]} - {url[original_url]} - {url[created]}'.format(url=url))

def action_show_menu():
    print('''
Сокращатель ссылок:
    1. Добавить url адрес
    2. Найти оригинальный url адрес
    3.Вывести все url адреса
    m. Показать меню
    q. Выйти''')

def action_exit():
    sys.exit(0)

actions = {
    'm': action_show_menu(),
    'q': action_exit()
}

#если этот файл используют как запускаемый
if __name__ == '__mailn__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        actions = actions.get(cmd)

        #если функция существует
        if action:
            action()
        else:
            print('Неизвестная команда')