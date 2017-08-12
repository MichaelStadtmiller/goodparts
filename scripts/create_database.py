import psycopg2
from config import config

def create_tables():
    commands = (
        """
        CREATE TABLE movie (
            id SERIAL PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            name_path VARCHAR(200) NOT NULL,
            description VARCHAR(200),
            poster VARCHAR(200),
            studio VARCHAR(200),
            genres VARCHAR(200),
            year_released INTEGER
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
            cur.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ = '__main__':
    create_tables()

