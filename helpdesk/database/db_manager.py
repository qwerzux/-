import sqlite3
from config import DB_NAME


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Пользователи
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT,
        phone TEXT
    )
    """)

    # Операторы
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        position TEXT,
        phone TEXT
    )
    """)

    # Обращения
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        operator_id INTEGER,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Новое',
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (operator_id) REFERENCES operators(id)
)
""")

    # Ответы
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id INTEGER NOT NULL,
        answer_text TEXT NOT NULL,
        FOREIGN KEY (ticket_id) REFERENCES tickets(id)
)
""")

    conn.commit()
    conn.close()