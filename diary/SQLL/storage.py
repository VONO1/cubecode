import sqlite3


SQL_SELECT = '''SELECT id, task_name, task_date, text, status FROM scheluder'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Инициализация базы
def initialize(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS scheluder (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_name TEXT NOT NULL DEFAULT '',
                task_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                text TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'Не выполнено'
            )
        ''')


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


# Добавление задачи к базе данных
def add_task(conn, task_name, task_date, text):
    with conn:
        cursor = conn.execute('''
            INSERT INTO scheluder (task_name, task_date, text) VALUES (?,?,?)
        ''', (task_name, task_date, text))


def find_by_id(conn, idx):
    with conn:
        cursor = conn.execute(SQL_SELECT + ''' WHERE id=?''', (idx,))
        return cursor.fetchone()


def update_task(conn, task_name, task_date, text, idx):
    with conn:
        cursor = conn.execute('''
            UPDATE scheluder SET task_name=?, task_date=?, text=? WHERE id=?
        ''', (task_name, task_date, text, idx))


def re_task(conn, idx):
    with conn:
        cursor = conn.execute('''
                UPDATE scheluder SET status='Не выполнено' WHERE id=?
            ''', idx)
        return

def close_task(conn, idx):
    with conn:
        cursor = conn.execute('''
                UPDATE scheluder SET status='Выполнено' WHERE id=?
            ''', idx)


def all_tasks(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()