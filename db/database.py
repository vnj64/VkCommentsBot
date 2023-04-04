import psycopg2
from config import load_config

config = load_config('.env')


def connect():
    conn = None
    try:
        print("Connecting to database.")

        conn = psycopg2.connect(
            host=config.db.host,
            password=config.db.password,
            user=config.db.user,
            dbname=config.db.database,
            port=config.db.port
        )

        cur = conn.cursor()

        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')

        db_version = cur.fetchone()

        print(db_version)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
