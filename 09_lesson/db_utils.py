import pandas as pd
from sqlalchemy import create_engine, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)


def query(sql, params=None):
    """Выполнить SQL запрос и вернуть результат"""
    with engine.connect() as conn:
        if params:
            result = conn.execute(text(sql), params)
        else:
            result = conn.execute(text(sql))
        conn.commit()
        return result


def show_tables():
    """Показать все таблицы"""
    df = pd.read_sql("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """, engine)
    print("Таблицы в базе данных:")
    print(df.to_string(index=False))
    return df


def show_table(table_name, limit=10):
    """Показать содержимое таблицы"""
    df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT {limit}", engine)
    print(f"Таблица: {table_name}")
    print(df.to_string(index=False))
    return df


def describe_table(table_name):
    """Показать структуру таблицы"""
    df = pd.read_sql("""
        SELECT
            column_name,
            data_type,
            is_nullable,
            column_default
        FROM information_schema.columns
        WHERE table_name = :table
        ORDER BY ordinal_position
    """, engine, params={"table": table_name})
    print(f"Структура таблицы {table_name}:")
    print(df.to_string(index=False))
    return df


print(" Модуль db_utils загружен. Доступные функции:")
print("  - query(sql) - выполнить SQL запрос")
print("  - show_tables() - показать все таблицы")
print("  - show_table('table_name') - показать данные")
print("  - describe_table('table_name') - структура таблицы")
