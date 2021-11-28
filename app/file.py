from db import Cursor


class File:
    def __init__(self, url=None, animal=None):
        self.url = url
        self.animal = animal

    def create_table(self):
        with Cursor() as cur:
            cur.execute(
                "CREATE TABLE files (\
                id serial not null,\
                url text not NULL,\
                animal text not NULL,\
                created_at TIMESTAMP DEFAULT NOW(),\
                updated_at TIMESTAMP DEFAULT NOW(),\
                PRIMARY KEY (id),\
                UNIQUE(url)\
                );"
            )

    @classmethod
    def get_by_random(cls):
        with Cursor() as cur:
            cur.execute("SELECT url FROM files ORDER BY RANDOM() limit 1")
            row = cur.fetchone()

            return cls(
                url=row[0],
            )

    @classmethod
    def get_by_animal(cls, animal: str):
        with Cursor() as cur:
            cur.execute(
                "SELECT url FROM files WHERE animal = %s ORDER BY RANDOM() limit 1",
                (animal,),
            )
            row = cur.fetchone()

            return cls(
                url=row[0],
            )

    def add(self, url: str, animal: str):
        with Cursor() as cur:
            cur.execute(
                "INSERT INTO files (url, animal) VALUES (%s, %s)",
                (
                    url,
                    animal,
                ),
            )

    def delete_by_url(self, url: str):
        with Cursor() as cur:
            cur.execute("DELETE FROM files WHERE url = %s", (url,))
