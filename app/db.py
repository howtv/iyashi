import os

import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv


if os.environ.get("ENVIRONMENT") is None:
    load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")


def _get_connection():
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(e)


def init():
    _create_table()
    # add_file("", animal.DOG)
    return


def _create_table():
    try:
        with _get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CREATE TABLE files (\
                    id serial not null,\
                    url text not NULL,\
                    animal text not NULL,\
                    created_at TIMESTAMP,\
                    updated_at TIMESTAMP,\
                    PRIMARY KEY (id),\
                    UNIQUE(url)\
                    );"
                )
            conn.commit()
    except Exception as e:
        print(e)


def get_file_by_animal(animal: str):
    try:
        with _get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "SELECT url FROM files WHERE animal = %s ORDER BY RANDOM() limit 1",
                    (animal,),
                )
                return cur.fetchone()
    except Exception as e:
        print(e)


def get_file_by_random():
    try:
        with _get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT url FROM files ORDER BY RANDOM() limit 1")
                return cur.fetchone()
    except Exception as e:
        print(e)


def add_file(url: str, animal: str):
    try:
        with _get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO files (url, animal) VALUES (%s, %s)",
                    (
                        url,
                        animal,
                    ),
                )
            conn.commit()
    except Exception as e:
        print(e)
