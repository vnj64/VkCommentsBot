import psycopg2
from config import host, password, user, name, port


def connect():
    conn = None
    try:
        print("Connecting to database.")

        conn = psycopg2.connect(
            host=host,
            password=password,
            user=user,
            dbname=name,
            port=port
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